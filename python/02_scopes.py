# variable defined directly in module has global scope

a = 1
print(globals().keys())

# you can use builtins module to access buildins methods like print

import builtins
print = 1
builtins.print(1)

del(print)

# when creating variable inside function it is creted in local scope

def person():
    name = "peter" # local scope
    print(name)

person()

# if I want to access global scope I use global keyword

name = "tomas"

def person():
    global name
    name = "tomas-modified" # modified global var
    print(name)

person()
print(name)

# combine
# this approach throws 

def person():
    print(name)
    name = "richard"
    print(name)

#person() # throws