cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2) #O(2^n)
    
    return cache[n]

for i in range(100):
    print(f"{i:3} {fib(i)}")



## hint: can use tuples as a key in a dictionary

def foo(a,x,b):

    cache[(a,x,b)] = ...