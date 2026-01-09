from keras import Sequential
from keras.layers import Input, Dense
from keras.activations import softmax
from keras.losses import CategoricalCrossentropy
from keras.optimizers import SGD, RMSprop, Adam
from keras.metrics import CategoricalAccuracy
from keras.utils import to_categorical

from matplotlib import pyplot as plt
from numpy import array
from PIL import Image

from pprint import pp

from mnist_load import x_train, x_test, y_train, y_test, script_dir


model = Sequential(
    [
        Input(shape=(784,)),
        Dense(units=64, activation='sigmoid', name='hidden'),
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
    verbose=0,
)

print()
test1_result = model.evaluate(
    x=x_test.reshape(x_test.shape[0], -1),
    y=to_categorical(y_test, num_classes=10),
    verbose=2,
)


test2_dir = script_dir / 'mnist/test'

test2_imgs = array([
    Image.open(p).convert(mode='L').getdata()
    for p in test2_dir.glob('*.png')
])
test2_lbls = array([
    int(p.name[0])
    for p in test2_dir.glob('*.png')
])

test2_result = model.predict(
    x=test2_imgs,
    verbose=1,
)
# >>> test2_result.argmax(axis=1)
# array([5, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 4, 8])

test2_ass = model.evaluate(
    x=test2_imgs,
    y=to_categorical(test2_lbls, num_classes=10),
    verbose=1,
)

