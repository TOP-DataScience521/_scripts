try:
    print(var)

except NameError as exception_object:
    print(type(exception_object))
    print(exception_object)


# >>> exception_object
# NameError("name 'var' is not defined")

