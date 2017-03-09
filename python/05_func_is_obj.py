# functions are objects
def sum(x,y):
    return x+y

print(dir(sum))
print(type(sum))

sum.a = "pycon"
sum.b = 5
sum.c = lambda: print("functions are objects")

sum.c()

# define attributes on object (function)

def myprint(msg):
    print(myprint.prefix, msg)

myprint.prefix = "pycon:"
myprint("hello world")
