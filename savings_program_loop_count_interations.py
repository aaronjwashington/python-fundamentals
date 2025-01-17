initial_savings = int(input())

interest_rate = float(input())

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest. \n'.format(interest_rate*100))

years = int(input('Enter years: '))

savings = initial_savings

i = 1 #loop variable

while i <= years: # Loop condition
    print(' Savings at begninning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1 # increment loop variable
    
print('\n')