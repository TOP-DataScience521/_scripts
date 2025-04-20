var = 123

print(
    '\nперывй вызов locals() из глобального пространства имён\n',
    locals(), 
    end='\n\n'
)


def test():
    var = 456
    print(
        '\nвызов locals() из локального пространства имён функции test()\n',
        locals(), 
        end='\n\n'
    )

test()


print(
    '\nвторой вызов locals() из глобального пространства имён\n',
    locals(), 
    end='\n\n'
)

