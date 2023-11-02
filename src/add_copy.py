import sys 

def add (a, b):
    return (a + b)

def add1 (a, b):
    return (a + b)

def add2 (a, b):
    return (a + b)

def sub (a, b):
    return (a - b)

def mul (a, b):
    return (a * b)

def dev (a, b):
    return (a / b)

def mod (a, b):
    return (a % b)

def sayhello():
    print("hello")

def calculate_square(number):
    return number ** 2

def calculate_cube(number):
    return number ** 3

def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


def calculate_factorial1(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


def calculate_factorial2(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
