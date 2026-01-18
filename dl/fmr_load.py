__all__ = (
    'x_train',
    'y_train',
    'x_test',
    'y_test',
)

from keras.utils import to_categorical
from numpy import array, zeros
from PIL import Image
from sklearn.model_selection import train_test_split

from pathlib import Path
from sys import path
from time import perf_counter


script_dir = Path(path[0])
fmr_dir = script_dir / 'fmr'

IMG_SIZE = (192, 108)

labels_classes = {car_dir.name: i for i, car_dir in enumerate(fmr_dir.iterdir())}


# формирование списков изображений, затем создание массивов на основе списков
# start = perf_counter()
# x, y = [], []
# 
# for car_dir in fmr_dir.iterdir():
#     for img_path in car_dir.iterdir():
#         with Image.open(img_path) as img:
#             # if img.size != IMG_SIZE:
#             #     print(f'{car_dir.name}/{img_path.name}')
#             #     img = img.resize(IMG_SIZE)
#             x.append(array(img))
#         y.append(labels_classes[car_dir.name])
# 
# x = array(x)
# y = to_categorical(y, num_classes=3)
# end = perf_counter()
# print(f'elapsed time: {(end - start)*1000:.0f} ms')
# elapsed time: 1320 ms


# создание массивов нолей, затем перезапись элементов массивов изображениями
start = perf_counter()
total_imgs = sum(1 for _ in fmr_dir.rglob('*.png'))

x = zeros(shape=(total_imgs, *IMG_SIZE[::-1], 3), dtype='uint8')
y = zeros(shape=(x.shape[0], 3), dtype='float32')

i = 0
for car_dir in fmr_dir.iterdir():
    for img_path in car_dir.iterdir():
        with Image.open(img_path) as img:
            # if img.size != IMG_SIZE:
            #     print(f'{car_dir.name}/{img_path.name}')
            #     img = img.resize(IMG_SIZE)
            x[i] = array(img)
        y[i,labels_classes[car_dir.name]] = 1
        i += 1
end = perf_counter()
print(f'elapsed time: {(end - start)*1000:.0f} ms')
# elapsed time: 1252 ms


x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.1,
    random_state=1,
    shuffle=True,
)

