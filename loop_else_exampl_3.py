result = 1
for n in range(4):
    print(n, end=' ')
    result *= 3
else:
    print('/ {}'.format(result))
print('done')