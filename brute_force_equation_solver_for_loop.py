''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

solution_found = True

''' Type your code here. '''
#For every value of x from -10 to 10
for x in range (-10, 11):
#   For every value of y from -10 to 10
    for y in range(-10, 11):
#      Check if the current x and y satisfy both equations. If so, output the solution, and finish.
        if (( a * x )+ (b * y)) == c and ((d * x) + (e * y)) == f:
            solution_found = True
            print(f"x = {x}, y = {y}")
            
if solution_found == False:
    print("There is no solution")