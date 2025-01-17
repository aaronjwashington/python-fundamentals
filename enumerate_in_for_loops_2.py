numbers = [3, -9, 9, -1, -6]
for (position, number) in enumerate(numbers):
    if number < 0:
        print(position, number)
    else:
        print(position, 'x')