import math

# Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

x = float(input())
y = float(input())
z = float(input())

value1 = x ** z
value2 = x ** (y ** z)
value3 = abs(x - y)
value4 = math.sqrt(x ** z)

print(f'{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}') # This will output only 2 decimal places.



