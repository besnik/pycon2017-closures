# closure over function
def counter(func):
    count = 0
    def inc_count():
        func()
        nonlocal count
        count += 1
        print("    Called", count, "times")
    return inc_count

def hello():
    print("Hi PyCon")

inc = counter(hello)
inc()
inc()
inc()

# closures over func
def create_logic(func):
    def when(a,b):
        if not (callable(a) and callable(b)):
            raise TypeError("Expecting callable for input parameters")
        return func(a,b)
    return when


_and = create_logic(lambda x,y: x() and y())
_or = create_logic(lambda x,y: x() or y())

validate1 = lambda: True
validate2 = lambda: False

print(_and(validate1, validate1))
print(_and(validate2, validate1))

# more complex composition
is_valid = _and(
    lambda: _or(validate1, validate2), 
    lambda: _and(validate1, validate1)
    )
print(is_valid)

#     and
#     / \
#   or   and
#  / \   / \
# v1 v2 v1 v1

