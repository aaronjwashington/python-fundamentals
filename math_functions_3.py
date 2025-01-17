import math

x = float(input())
y = float(input())

# z = √|x|-|y|

z = math.sqrt(math.fabs(x) - math.fabs(y))

print(round(z, 2))