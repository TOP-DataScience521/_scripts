def options_handler(**options):
    print(type(options), options, sep='\n')
    ...


# >>> options_handler(123)
# TypeError: options_handler() takes 0 positional arguments but 1 was given


# >>> options_handler()
# <class 'dict'>
# {}
# >>>
# >>>
# >>> options_handler(num=123)
# <class 'dict'>
# {'num': 123}
# >>>
# >>>
# >>> options_handler(num=123, ab_12_cd=range(2, 5))
# <class 'dict'>
# {'num': 123, 'ab_12_cd': range(2, 5)}

