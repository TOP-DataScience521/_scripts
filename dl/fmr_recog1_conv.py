from keras import Sequential
from keras.layers import (
    BatchNormalization, 
    Conv2D, 
    Dense, 
    Dropout, 
    Flatten, 
    Input, 
    MaxPooling2D,
)
from keras.activations import relu, sigmoid, softmax
from keras.losses import CategoricalCrossentropy
from keras.optimizers import Adam
from keras.metrics import CategoricalAccuracy

from matplotlib import pyplot as plt

from fmr_load import *
from fmr_load import script_dir


model = Sequential(
    [
        Input(shape=(108, 192, 3)),
        Conv2D(
            filters=32, 
            kernel_size=(5, 5), 
            activation=relu, 
            use_bias=True, 
            name='low-level_features_map'
        ),
        BatchNormalization(),
        # Activation(lambda x: relu(x, slope=0.5)),
        MaxPooling2D(pool_size=(2, 2), name='subsampling_1'),
        Conv2D(
            filters=64, 
            kernel_size=(3, 3), 
            activation=relu, 
            use_bias=True, 
            name='mid-level_features_map'
        ),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2), name='subsampling_2'),
        Conv2D(
            filters=64, 
            kernel_size=(3, 3), 
            activation=relu, 
            use_bias=True, 
            name='high-level_features_map'
        ),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2), name='subsampling_3'),
        Flatten(name='vectorization'),
        Dropout(rate=0.5, name='random_weights_exclusion'),
        Dense(units=16, activation=relu, use_bias=True, name='classifier_dense_1'),
        Dense(units=3, activation=softmax, use_bias=True, name='classifier_output'),
    ], 
    name='car_recognition'
)
print()
model.summary()

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(),
    metrics=[
        CategoricalAccuracy(name='acc'),
    ]
)

print()
fit_result = model.fit(
    x=x_train,
    y=y_train,
    epochs=100,
    verbose=2,
)

print()
test_result = model.evaluate(
    x=x_test,
    y=y_test,
    verbose=2,
)


fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(1, 2)

axs[0].plot(fit_result.epoch, fit_result.history['acc'], lw=2)
axs[0].scatter(fit_result.epoch[-1] + 1, test_result[1], c='#d11')

axs[1].plot(fit_result.epoch, fit_result.history['loss'], lw=2)
axs[1].scatter(fit_result.epoch[-1] + 1, test_result[0], c='#d11')

fig.savefig(script_dir / 'fmr output/3-conv-layers_32-64-64_100-epochs.png')


