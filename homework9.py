# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string
# (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної
# успішної операції add або delete.


my_contacts = {
    'Wednesday Addams': '+442255667788',
    'Gregory House': '+112233445566',
    'Winston Churchill': '+445566778899'
}
import json

json_phone_book = json.dumps(my_contacts)
print(json_phone_book)
with open('json', 'w') as file:
    file.write(json_phone_book)

while True:
    command = input("Enter command (stats, add, delete, list, show): ")
    # format "command amount"

    if command == 'stats':
        with open('json') as file:
            new_contact_book = file.read()
            my_contacts = json.loads(new_contact_book)
        print(len(my_contacts))
    # calculating the number of contacts

    elif command == 'add':
        new_contact_name = input('Type name and surname: ')
        if new_contact_name in my_contacts:
            print("This contact is already in the contact list.")
        else:
            new_contact_phone = input('Type phone number: ')
            my_contacts[new_contact_name] = new_contact_phone
            print(my_contacts)
            with open('json', 'a') as file:
                file.write(json_phone_book)
                new_contact_book = file.read()
                my_contacts = json.loads(new_contact_book)
    # adding new contact

    elif command == 'delete':
        contact_to_delete = input('Enter name and surname: ')
        if contact_to_delete in my_contacts:
            del my_contacts[contact_to_delete]
            print(my_contacts)
            with open('json', 'a') as file:
                file.write(json_phone_book)
                new_contact_book = file.read()
                my_contacts = json.loads(new_contact_book)
        else:
            print("This contact does not exist. Nothing to delete.")
    # deleting contact by name

    elif command == 'list':
        for key, value in my_contacts.items():
            print(key, value)
    # printing the contact list

    elif command == 'show':
        contact_to_show = input('Enter name and surname: ')
        if contact_to_show in my_contacts:
             print(my_contacts[contact_to_show])
        else:
            print("This contact does not exist.")
    # showing phone number by name and surname
    else:
        print('Wrong command')

# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

