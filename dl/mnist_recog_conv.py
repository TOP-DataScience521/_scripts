from keras import Sequential
from keras.layers import Input, Conv2D, Dense, Flatten
from keras.activations import relu, softmax
from keras.losses import CategoricalCrossentropy
from keras.optimizers import Adam
from keras.metrics import CategoricalAccuracy
from keras.utils import to_categorical

from matplotlib import pyplot as plt
from numpy import array
from PIL import Image

from mnist_load import x_train, x_test, y_train, y_test, script_dir


buffer = []
def capture_to_buffer(string):
    buffer.append(string)


model = Sequential(
    [
        Input(shape=(28, 28, 1)),
        Conv2D(filters=8, kernel_size=(3, 3), activation=relu, use_bias=False),
        Flatten(),
        Dense(units=10, activation=softmax, use_bias=False),
    ], 
    name='digits_recognition_convolution'
)
print()
# в stdout
model.summary()
# в buffer
model.summary(print_fn=capture_to_buffer)

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(),
    metrics=[
        CategoricalAccuracy(name='acc'),
    ]
)

print()
epochs = 12
fit_result = model.fit(
    x=x_train.reshape(*x_train.shape, 1),
    y=to_categorical(y_train, num_classes=10),
    epochs=epochs,
    verbose=2,
)

print()
test1_result = model.evaluate(
    x=x_test.reshape(*x_test.shape, 1),
    y=to_categorical(y_test, num_classes=10),
    verbose=2,
)


fig = plt.figure(figsize=(12, 9))
axs_dict = fig.subplot_mosaic(
    mosaic=[
        ['text', 'text'],
        ['acc_plot', 'loss_plot'],
    ],
    gridspec_kw={
        'width_ratios': [1, 1], 
        'height_ratios': [1, 1.5]
    }
)

axs_dict['text'].set_axis_off()
axs_dict['text'].text(
    0, 0, 
    '\n'.join(buffer), 
    fontfamily='Hack', fontsize=14,
    transform=axs_dict['text'].transAxes
)

axs_dict['acc_plot'].plot(fit_result.epoch, fit_result.history['acc'], lw=2)
axs_dict['acc_plot'].scatter(fit_result.epoch[-1] + 1, test1_result[1], c='#d11')

axs_dict['loss_plot'].plot(fit_result.epoch, fit_result.history['loss'], lw=2)
axs_dict['loss_plot'].scatter(fit_result.epoch[-1] + 1, test1_result[0], c='#d11')

fig.savefig(script_dir / f'mnist/1-conv-layer_8_adam_{epochs}-epochs.png')



test2_dir = script_dir / 'mnist/test'

test2_imgs = array([
    Image.open(p).convert(mode='L')
    for p in test2_dir.glob('*.png')
])
test2_lbls = array([
    int(p.name[0])
    for p in test2_dir.glob('*.png')
])

print()
test2_result = model.predict(
    x=test2_imgs.reshape(*test2_imgs.shape, 1),
    verbose=2,
)
# >>> test2_result.argmax(axis=1)
# array([0, 0, 0, 7, 1, 6, 1, 1, 2, 2, 8, 4, 8])

print()
test2_ass = model.evaluate(
    x=test2_imgs.reshape(*test2_imgs.shape, 1),
    y=to_categorical(test2_lbls, num_classes=10),
    verbose=2,
)


