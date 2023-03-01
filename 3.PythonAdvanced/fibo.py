import random

# Fibonacci numbers module

secret_value = random.randint(1, 100)

def fib(n):
    """
       Write Fibonacci seried up to n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """
        Return Fibonacci series up to n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result