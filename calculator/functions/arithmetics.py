"""Arithmetic helpers."""

def summe(a, b):
    return a + b

def multiplikation(a, b):
    return a * b

def subtraktion(a, b):
    return a - b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
