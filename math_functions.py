import math

# compute z = (√x*y)^5

x = float(input())
y = float(input())

z = math.pow(math.sqrt(x * y), 5)

print(round(z, 2)) # This will output only 2 decimal places.



