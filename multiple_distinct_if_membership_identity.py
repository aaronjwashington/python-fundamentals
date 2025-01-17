#user_age = int(input('Enter age:'))


# Note that more than one "if" statement can execute

#if user_age < 16:
    #print('Enjoy your early years.')
    
#if user_age > 15:
    #print('You are old enough to drive.')
    
#if user_age > 17:
    #print('You are old enough to vote.')

#if user_age > 24:
    #print('Most car rental companies will rent to you.')
    
#if user_age > 34:
    #print('You can run for president')


    
# Membership operators can be used  with sequences
    
#barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

#name = input('Enter name to check: ')

#if name in barcelona_fc_roster:
    #print('Found', name, 'on the roster.')
#else:
    #print('Could not find', name, 'on the roster.')
    

# Use the "not in" operator
#barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

#name = input('Enter name to check: ')

#if name not in barcelona_fc_roster:
    #print('Could not find', name, 'on the roster.')
#else:
    #print('Found', name, 'on the roster.')


    
# Checking for substrings

#request_str = 'GET index.html HTTP/1.1'

#if '/1.1' in request_str:
    #print('HTTP protocol 1.1')

#if 'HTTPS' not in request_str:
    #print('Unsecured connection')


    
# Checking for membership in a dict

my_dict = {'A' : 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
    print("'Found B'")
else:
    print("'B' not found")
    
# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')