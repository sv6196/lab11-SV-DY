import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b


def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Value to take logarithm of must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a**b
