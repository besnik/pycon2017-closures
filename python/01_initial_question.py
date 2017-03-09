# This code has one problem

funcs = []
for i in range(0, 10):
    funcs.append(lambda: print(i))

for f in funcs:
    f()

