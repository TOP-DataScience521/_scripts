print('начало выполнения module3')

num = 1357
year = 2030

def show_namespace():
    print({
        k: v
        for k, v in globals().items()
        if not k.startswith('__')
    })

print('конец выполнения module3')