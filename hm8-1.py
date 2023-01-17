# 1 Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.
# importing library
import time
import math


# decorator to calculate curent time when function is called
def calculate_time(func):
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.localtime()

        func(*args, **kwargs)

        print(f"The function {func.__name__}, called at {begin.tm_hour}:{begin.tm_min}.")

    return inner1


# function example
@calculate_time
def squareRoot(num):
    print(math.sqrt(num))


# calling the function.
squareRoot(20)
