# does this code throw ?
def outer():
    var = 1

    def inner():
        var += 1

    return inner

# yes - because python requres you to define scope for var inside inner (nonlocal vs local)
#outer()()

# how to fix the below code?
print("original")
funcs = []
for i in range(0, 10):
    funcs.append(lambda: print(i))

for f in funcs:
    f()

# storing value in separate local var of the outer scope won't help as closures are closing around variable (not value!) and variable in the end of first cycle has value 9
print("wrong")
def setup_funcs():
    funcs = []
    for i in range(0, 10):
        j = i
        funcs.append(lambda: print(j))
    return funcs

funcs = setup_funcs()
for f in funcs:
    f()

import dis
dis.dis(setup_funcs)

#solutions

print("solution 1")
# variant 3
funcs = []
for i in range(0, 10):
    funcs.append(lambda x=i: print(x))

for f in funcs:
    f()

print("solution 2")
funcs = []
for i in range(0, 10):
    def myprint(i=i):
        print(i)
    funcs.append(myprint)

for f in funcs:
    f()

print("solution 3")
# variant 2
funcs = []
for i in range(0, 10):
    funcs.append((lambda i: lambda: print(i))(i))

for f in funcs:
    f()

print("solution 3 - classic")
# variant 1
funcs = []
for i in range(0, 10):
    def outer(x):
        return lambda: print(x)
    funcs.append(outer(i))

for f in funcs:
    f()

print("solution 4")
funcs = []
for i in range(0, 10):
    (lambda i: funcs.append(lambda: print(i)))(i)

for f in funcs:
    f()

print("solution 4 - classic")
funcs = []
for i in range(0, 10):
    def outer(i):
        funcs.append(lambda: print(i))
    outer(i)

for f in funcs:
    f()

print("version 5")
# variant 4
funcs = [(lambda x: lambda: print(x))(x) for x  in range(1,10)]

for f in funcs:
    f()

# works
print("version 6")
# variant 5
class Func:
    def __init__(self, i): self.i = i
    def __call__(self): print(self.i)

funcs = [Func(i) for i in range(1,10)]

for f in funcs:
    f()

# closures closes over variables, not values
# during func execution time value of closed variable is used, not during declaration time