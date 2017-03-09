# define parameterless lambda

f1 = lambda: print("hi pycon")
f2 = lambda x: x*x
f3 = lambda x,y: x+y
f4 = lambda i: i > 5

f1()
print(f2(5))
print(f3(2,2))
print(f4(8))

# define and immediately call lambda
print((lambda x: x*x)(5))

# define lambda everywhere

def test():
    sum = lambda a,b: a+b
    x = 3
    y = 2
    print(sum(3,2))

test()
