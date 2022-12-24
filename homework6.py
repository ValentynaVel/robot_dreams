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

command = input("Enter command (stats, add, delete, list, show): ")
# format "command amount"

if command == 'stats':
    print(len(my_contacts))
    # calculating the number of contacts

elif command == 'add':
    new_contact_name = input('Type name and surname: ')
    new_contact_phone = input('Type phone number: ')
    my_contacts[new_contact_name] = new_contact_phone
    print(my_contacts)
    # adding new contact

elif command == 'delete':
    contact_to_delete = input('Enter name and surname: ')
    del my_contacts[contact_to_delete]
    print(my_contacts)
    # deleting contact by name

elif command == 'list':
    for key, value in my_contacts.items():
        print(key, value)
    # printing the contact list

elif command == 'show':
    contact_to_show = input('Enter name and surname: ')
    print(my_contacts[contact_to_show])
    # showing phone number by name

else:
    print('Wrong command')

