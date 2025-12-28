from numpy import load

from pathlib import Path
from sys import path


script_dir = Path(path[0])
mnist_path = script_dir / 'mnist.npz'


with load(mnist_path) as data:
    x_train, x_test = data['x_train'], data['x_test']
    y_train, y_test = data['y_train'], data['y_test']

# >>> print(x_train.shape, y_train.shape)
# (60000, 28, 28) (60000,)
# >>> 
# >>> print(x_test.shape, y_test.shape)
# (10000, 28, 28) (10000,)



if __name__ == '__main__':
    
    from matplotlib import pyplot as plt
    
    fig = plt.figure(figsize=(4, 4))
    axs = fig.subplots()
    
    axs.imshow(x_train[0], cmap='gray')
    
    fig.show()
    
    # >>> print(f'{y_train[0] = !s}')
    # y_train[0] = 5
    
    
    from numpy import concat
    from PIL import Image
    
    mnist_dir = script_dir / 'mnist/imgs'
    mnist_dir.mkdir(parents=True, exist_ok=True)
    
    for i, matr in enumerate(concat([x_train, x_test]), 1):
        img = Image.fromarray(matr, mode='L')
        img.save(mnist_dir / f'dig{i:0>5}.png')

