result = 1
n = 3
while n < 9:
    print(n, end=' ')
    result *= 4
    if result > 38:
        print('*')
        break
    n += 1
else:
    print('/ {}'.format(result))
print('done')

