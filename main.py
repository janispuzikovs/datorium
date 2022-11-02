#Please let us go to home!

contacts = []

person_name = input('Name: ')
person_surname = input('Surname: ') 
person_phone = input('Phone: ')
person_email = input('Email: ')

person_data = {
  'name': person_name,
  'surname': person_surname,
  'phone': person_phone,
  'email': person_email
}

contact_anna = {
  'name': 'Anna',
  'surname': 'Bērziņa',
  'phone': '+371 28472133',
'email': 'anna_b@somemail.com'
}

while(True):
    response = input('(1)add contact (2)print contacts (3)exit: ')
    
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_data = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }

        contacts.append(person_data)
    elif response == '2':
        print(contacts)
    elif response == '3':
        print('Bye bye 🥰')
        exit()

print(contacts)