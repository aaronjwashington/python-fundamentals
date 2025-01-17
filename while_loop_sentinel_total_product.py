entered_age = int(input())


while (entered_age < 18 or entered_age > 40):
    if entered_age < 18:
        print('Very young')
    else:
        print('Grown up')
    entered_age = int(input())
    
print('Perfect match', end='')