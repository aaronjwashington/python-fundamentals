contact_emails = {'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()

contact_emails[new_contact] = new_email
for contact, email in contact_emails.items():
    print('{} is {}'.format(email, contact))