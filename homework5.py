# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”

user_input = input('Type something: ')
for item in user_input:
    if item.isdigit():
        if int(item) % 2 == 0:
            print(f'This is digit {item}. It is even.')
        else:
            print(f'This is digit {item}. It is odd.')
    elif item.isalpha():
        if item.isupper():
            print(f'This is letter {item}. It is capitalized.')
        else:
            print(f'This is letter {item}. It is not capitalized.')
    else:
        print('This is a symbol')

# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, поки її виконання не буде перервано вручну.
# Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати бібліотеку time (import time), а саме функцію sleep().
# (time.sleep(second), де second, це кількість секунд, які програма має чекати).

import time
# import time module

while True:
    print('I love Python')
    time.sleep(4.2)
