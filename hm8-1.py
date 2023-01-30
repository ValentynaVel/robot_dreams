# 1 Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

# importing library
import time
import math

# decorator to calculate current time when function is called


def calculate_time(func):

    def wrap(*args, **kwargs):
        # storing time before function call
        begin = time.localtime()
        res = func(*args, **kwargs)
        print(f"The function {func.__name__}, called at {begin.tm_hour}:{begin.tm_min}.")
        return res
    return wrap


# function example
@calculate_time
def squareRoot(num):
    print(math.sqrt(num))


# calling the function.
squareRoot(40)
