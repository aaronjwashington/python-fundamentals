import math

x = float(input())
y = float(input())

# z = √|x|^y

z = math.sqrt(math.pow(math.fabs(x), y ))

print(round(z, 2))