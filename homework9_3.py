# 3. В попередньо написаний кастомний Exception додати запис помилки і час її
# виникнення у файл.

from datetime import datetime


class MyCustomExeption(Exception):
    def __init__(self, message=f'Exception: Incorrect password.'):
        self.message = message
        with open('mistakes.txt', 'a') as print_file:
            print(f'{self.message}, time: {datetime.now().isoformat()}', file=print_file)


password = 1234

try:
    input_password = int(input("Enter a password: "))
    if input_password != password:
        msg = MyCustomExeption()
    else:
        print("Eligible to enter the meeting.")

except MyCustomExeption():
    raise MyCustomExeption

