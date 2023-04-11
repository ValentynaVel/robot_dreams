# Task description:
# 1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є введений текст “числом” чи “словом”.
# 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
# 3. Якщо це “слово”, програма має вказати його довжину.

user_input = input("Enter number or word: ")

if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print("This is number " + str(number) + ". It is even.")
    else:
        print("This is number " + str(number) + ". It is odd.")
else:
    print("This is word. It contains " + str(len(user_input)) + " letters.")













