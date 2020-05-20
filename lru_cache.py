from functools import lru_cache

@lru_cache(maxsize = 1_000)
def fibonacci(n):
    # Check if it's a positive integer
    if type(n) != int: raise TypeError("N must be a positive integer!")
    if n<1: raise ValueError("N must be a positive integer!")

    if n == 1 or n==2: return 1
    elif n>2: return fibonacci(n-1) + fibonacci(n-2)
