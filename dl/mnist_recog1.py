from keras import Sequential
from keras.layers import Input, Dense
from keras.activations import softmax
from keras.losses import CategoricalCrossentropy
from keras.optimizers import SGD, RMSprop, Adam
from keras.metrics import CategoricalAccuracy
from keras.utils import to_categorical

from matplotlib import pyplot as plt

from pprint import pp

from mnist_load import x_train, x_test, y_train, y_test, script_dir


# унитарное кодирование (one-hot encoding)
# 0 —> [1 0 0 0 0 0 0 0 0 0]
# 1 —> [0 1 0 0 0 0 0 0 0 0]
# 2 —> [0 0 1 0 0 0 0 0 0 0]
# 3 —> [0 0 0 1 0 0 0 0 0 0]
# 4 —> [0 0 0 0 1 0 0 0 0 0]
# 5 —> [0 0 0 0 0 1 0 0 0 0]
# 6 —> [0 0 0 0 0 0 1 0 0 0]
# 7 —> [0 0 0 0 0 0 0 1 0 0]
# 8 —> [0 0 0 0 0 0 0 0 1 0]
# 9 —> [0 0 0 0 0 0 0 0 0 1]


model = Sequential(
    [
        Input(shape=(784,)),
        Dense(units=64, activation='sigmoid', name='hidden1'),
        Dense(units=10, activation='softmax', name='output'),
    ], 
    name='digits_recognition'
)
print()
model.summary()

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=SGD(),
    metrics=[
        CategoricalAccuracy(name='acc'),
    ]
)

x_train_prep = x_train.reshape(x_train.shape[0], -1)
y_train_prep = to_categorical(y_train, num_classes=10)
print()
fit_result = model.fit(
    x=x_train_prep,
    y=y_train_prep,
    epochs=100,
    verbose=2,
)

print()
test_result = model.evaluate(
    x=x_test.reshape(x_test.shape[0], -1),
    y=to_categorical(y_test, num_classes=10),
    verbose=2,
)


fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(1, 2)

axs[0].plot(fit_result.epoch, fit_result.history['acc'], lw=2)
axs[0].scatter(fit_result.epoch[-1] + 1, test_result[1], c='#d11')

axs[1].plot(fit_result.epoch, fit_result.history['loss'], lw=2)
axs[1].scatter(fit_result.epoch[-1] + 1, test_result[0], c='#d11')

fig.savefig(script_dir / 'mnist/2-layer_64-10_sgd_100-epochs.png')

