def func1():
    print(1)


def func2():
    breakpoint()
    print(2)
    func1()
    print(2)


def func3():
    print(3)
    func2()
    print(3)


def func4():
    print(4)
    func3()
    print(4)


func4()


# ...cmd... > python stack1.py
# 4
# 3
# 
# > stack1.py(7) func2()
#   -> print(2)
# 
# (Pdb) ll
#   5     def func2():
#   6         breakpoint()
#   7  ->     print(2)
#   8         func1()
#   9         print(2)
# 
# (Pdb) where
# 
#   stack1.py(24) <module>()
#   -> func4()
# 
#   stack1.py(20) func4()
#   -> func3()
# 
#   stack1.py(14) func3()
#   -> func2()
# 
# > stack1.py(7) func2()
#   -> print(2)
# 
# (Pdb) step
# 2
# 
# > stack1.py(8) func2()
#   -> func1()
# 
# (Pdb) step
# 
# --Call--
# > stack1.py(1) func1()
#   -> def func1():
# 
# (Pdb) step
# 
# > stack1.py(2) func1()
#   -> print(1)
# 
# (Pdb) ll
#   1     def func1():
#   2  ->     print(1)
# 
# (Pdb) where
# 
#   stack1.py(24) <module>()
#   -> func4()
# 
#   stack1.py(20) func4()
#   -> func3()
# 
#   stack1.py(14) func3()
#   -> func2()
# 
#   stack1.py(8) func2()
#   -> func1()
# 
# > stack1.py(2) func1()
#   -> print(1)
# 
# (Pdb) step
# 1
# 
# --Return--
# > stack1.py(2) func1()-->None
#   -> print(1)
# 
# (Pdb) step
# 
# > stack1.py(9) func2()
#   -> print(2)
# 
# (Pdb) where
# 
#   stack1.py(24) <module>()
#   -> func4()
# 
#   stack1.py(20) func4()
#   -> func3()
# 
#   stack1.py(14) func3()
#   -> func2()
# 
# > stack1.py(9) func2()
#   -> print(2)
# 
# (Pdb) next
# 2
# 
# --Return--
# > stack1.py(9) func2()-->None
#   -> print(2)
# 
# (Pdb) next
# 
# > stack1.py(15) func3()
#   -> print(3)
# 
# (Pdb) where
# 
#   stack1.py(24) <module>()
#   -> func4()
# 
#   stack1.py(20) func4()
#   -> func3()
# 
# > stack1.py(15) func3()
#   -> print(3)
# 
# (Pdb) ll
#  12     def func3():
#  13         print(3)
#  14         func2()
#  15  ->     print(3)
# 
# (Pdb) next
# 3
# 
# --Return--
# > stack1.py(15) func3()-->None
#   -> print(3)
# 
# (Pdb) next
# 
# > stack1.py(21) func4()
#   -> print(4)
# 
# (Pdb) where
# 
#   stack1.py(24) <module>()
#   -> func4()
# 
# > stack1.py(21) func4()
#   -> print(4)
# 
# (Pdb) next
# 4
# 
# --Return--
# > stack1.py(21) func4()-->None
#   -> print(4)
# 
# (Pdb) next
# 
# --Return--
# > stack1.py(24) <module>()-->None
#   -> func4()
# 
# (Pdb) continue

