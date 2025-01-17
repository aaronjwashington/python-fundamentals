# Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f}'.format(your_value))

caffeine_mg = float(input())

after_6_hours = caffeine_mg / 2
after_12_hours = after_6_hours / 2
after_24_hours = after_12_hours / 4


print(f'After 6 hours: {after_6_hours:.2f} mg')
print(f'After 12 hours: {after_12_hours:.2f} mg')
print(f'After 24 hours: {after_24_hours:.2f} mg')