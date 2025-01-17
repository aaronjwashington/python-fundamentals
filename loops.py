# Writing a for loop

#x = ['a','b','c']
#for w in x:
    #print(w, end= '')

#Writing a loop with reversed()

#a = [1,2,3,4,5]
#for x in reversed(a):
     #print(x, end='')

#Face printing loop that exits on 'q'

nose = '0' # looks like a nose
user_value = '-'

while user_value != 'q':
    print(' {} {} '.format(user_value, user_value)) #print eyes
    print('  {}   '.format(nose))  #print nose
    print(user_value*5)  # Print mouth
    print('\n')
    
    # Get new char for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]
    
print('Goodbye.\n')
