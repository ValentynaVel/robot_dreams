# 1. Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.

my_contacts = {
    'Wednesday Addams': '+442255667788',
    'Gregory House': '+112233445566',
    'Winston Churchill': '+445566778899'
}

while True:
    command = input("Enter command (stats, add, delete, list, show): ")
    # format "command amount"

    if command == 'stats':
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
    # adding new contact

    elif command == 'delete':
        contact_to_delete = input('Enter name and surname: ')
        if contact_to_delete in my_contacts:
            del my_contacts[contact_to_delete]
            print(my_contacts)
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


