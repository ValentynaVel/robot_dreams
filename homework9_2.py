# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

# importing library
import time
import math
# decorator to calculate current time when function is called


def calculate_time(func):
    def wrap(*args, **kwargs):
        # storing time before function call
        begin = time.localtime()
        res = func(*args, **kwargs)
        with open('text.txt', 'a') as print_file:
            print(f"The function {func.__name__}, called at {begin.tm_hour}:{begin.tm_min}.", file=print_file)
        return res
    return wrap


# function example
@calculate_time
def square_root(num):
    print(math.sqrt(num))


# calling the function.
square_root(20)

