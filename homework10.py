# До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону
# за допомогою RegEx. Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX,
# 0XXXXXXXXX

import json
import re


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
            res = re.fullmatch("\+380\d{9}|380\d{9}|0\d{9}", new_contact_phone)
            if res:
                dic_phone_book[new_contact_name] = new_contact_phone
            else:
                print("Phone number format is not correct")
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
