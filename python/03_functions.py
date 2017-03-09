# pass function as parameter
l = [x for x in range(1,10)]

def condition(item):
    return item > 5

l2 = list(filter(condition, l))
print(l2)

# assign function to variable
c = condition
p = print

p("Hello World")
print(list(filter(c,l)))

# return functions
def create_print():
    return print

p = create_print()
p("Hi all")

# return functions
def create_print():
    def pycon_print(msg):
        print("pycon:", msg)
    return pycon_print

p = create_print()
p("Hi all")

