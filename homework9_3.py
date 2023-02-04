# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

import traceback
import datetime


class MyCustomExeption(Exception):
    "Raised when the input password is not correct."
    pass

password = 1234

try:
    input_password = int(input("Enter a password: "))
    if input_password != password:
        raise MyCustomExeption
    else:
        print("Eligible to enter the meeting.")

except MyCustomExeption:
    with open('mistakes.txt', 'a') as print_file:
        print(f'Exception: Incorrect password. Time of exception: ', file=print_file)


