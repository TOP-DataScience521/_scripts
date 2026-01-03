from keras import Sequential
from keras.layers import Input, Dense
from keras.activations import softmax
from keras.losses import CategoricalCrossentropy
from keras.optimizers import SGD, RMSprop, Adam
from keras.metrics import CategoricalAccuracy
from keras.utils import to_categorical

from mnist_load import x_train, x_test, y_train, y_test


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


model = Sequential([
    Input(shape=(784,)),
    Dense(units=10, activation='softmax'),
])
model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=SGD(),
    metrics=[
        CategoricalAccuracy(),
    ]
)

x_train_prep = x_train.reshape(x_train.shape[0], -1)
y_train_prep = to_categorical(y_train, num_classes=10)
model.fit(
    x=x_train_prep,
    y=y_train_prep,
    epochs=10,
    verbose=2,
)

model.evaluate(
    x=x_test.reshape(x_test.shape[0], -1),
    y=to_categorical(y_test, num_classes=10),
    verbose=2,
)

