movie_ticket_price = None

user_age = int(input('Enter your age: '))

if user_age <= 12:     # Age 12 and under
    print('Child ticket discount.')
    movie_ticket_price = 11
elif user_age >= 65:   # Age 65 and older
    print('Senior ticket discount.')  
    movie_ticket_price = 12
else:                  # All other ages
    movie_ticket_price = 14

print('Movie ticket price: ${}'.format(
       movie_ticket_price))

# Explicit Ranges with gaps detection using logical AND and OR

if (office_num >= 100 and office_num <= 150) or (office_num >= 200 and office_num <= 250):
    # valid office number

else:
    # invalid office number