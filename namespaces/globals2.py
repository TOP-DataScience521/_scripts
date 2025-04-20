var = 123


def show_current_module_namespace():
    for identificator, value in globals().items():
        print(f'{identificator!r}: {value!r}')


show_current_module_namespace()


current_module_namespace = {
    identificator: value
    for identificator, value in globals().items()
    if not identificator.startswith('__')
}

