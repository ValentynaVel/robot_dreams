# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string
# (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної
# успішної операції add або delete.

import json
my_contacts = {
    'Wednesday Addams': '+442255667788',
    'Gregory House': '+112233445566',
    'Winston Churchill': '+445566778899'
}

json_phone_book = json.dumps(my_contacts)

with open('phone_book.txt', 'w') as file:
    file.write(json_phone_book)
# creating file with contacts

with open('phone_book.txt') as file:
    new_json_data = file.read()
dic_phone_book = json.loads(new_json_data)
# loading contacts from file to dic

while True:
    command = input("Enter command (stats, add, delete, list, show): ")
    # format "command amount"

    if command == 'stats':
        print(len(dic_phone_book))
    # calculating the number of contacts

    elif command == 'add':
        new_contact_name = input('Type name and surname: ')
        if new_contact_name in dic_phone_book:
            print("This contact is already in the contact list.")
        else:
            new_contact_phone = input('Type phone number: ')
            dic_phone_book[new_contact_name] = new_contact_phone
            print(dic_phone_book)
            add_json_phone_book = json.dumps(dic_phone_book)
            with open('phone_book.txt', 'w') as file:
                file.write(add_json_phone_book)
    # adding new contact

    elif command == 'delete':
        contact_to_delete = input('Enter name and surname: ')
        if contact_to_delete in dic_phone_book:
            del dic_phone_book[contact_to_delete]
            print(dic_phone_book)
            del_json_phone_book = json.dumps(dic_phone_book)
            with open('phone_book.txt', 'w') as file:
                file.write(del_json_phone_book)
        else:
            print("This contact does not exist. Nothing to delete.")
    # deleting contact by name

    elif command == 'list':
        for key, value in dic_phone_book.items():
            print(key, value)
    # printing the contact list

    elif command == 'show':
        contact_to_show = input('Enter name and surname: ')
        if contact_to_show in dic_phone_book:
            print(dic_phone_book[contact_to_show])
        else:
            print("This contact does not exist.")
    # showing phone number by name and surname
    else:
        print('Wrong command')



