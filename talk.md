# Introduction

This presentation tries to explain closures concept in bottom-up way. 
We believe that understanding basic priciples of language, compiler and runtime 
will help you naturaly understand closure and better understand language in general.

# Pool

Does audience understand python, java, c#, javascript or node.js ?
If yes at what level?

# Initial question

We are going to introduce relatively simple code that have one problem.
By end of the talk the audience should have solid understanding what is going on
and how to solve the problem.

```
# This code has one problem

funcs = []
for i in range(0, 10):
    funcs.append(lambda: print(i))

for f in funcs:
    f()
```

# Scopes

Not all variables are accessible from all parts of our program, and not all variables exist for the same amount of time. Where a variable is accessible and how long it exists depend on how it is defined. We call the part of a program where a variable is accessible its scope, and the duration for which the variable exists its lifetime.

Read more here: http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html

Local vs Global scope
builtins module

# Functions as first class citizens

Passing functions as parameter
Returning function



