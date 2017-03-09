# where are free variables stored
def create_condition(limit):
    return lambda item: item > limit

c1 = create_condition(5)
c2 = create_condition(10)

print(c1(4))
print(c1(6))

print(c1.__closure__) # (<cell at 0x7fc301eeb708: int object at 0xa68ac0>,)
print(c1.__closure__[0].cell_contents) # 5
