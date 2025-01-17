stop = -14
total = 0
for number in [7, 6, 3, 2, 6, 7]:
    print(number, end=' ')
    total -= number
    if total < stop:
        print('*')
        break
else:
    print('/ {}'.format(total))
print('done')