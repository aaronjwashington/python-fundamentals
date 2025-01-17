Task:
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

Employee A: 15.62 miles
Employee B: 41.85 miles
Employee C: 32.67 miles
The solution output should be in the format



#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places
Employee_A = float(input())
Employee_B = float(input())
Employee_C = float(input())

total_miles_traveled = (Employee_A + Employee_B + Employee_C)

print('Distance: {:.2f} miles'.format(total_miles_traveled))


#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

total_oz = int(input())

tons = total_oz // 32000

pounds = (total_oz % 32000) // 16

ounces = total_oz % 16

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")

    
    
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

value = int(input())

z = various_data_types[value]

data_type = type(z).__name__
print(f"Element{value}: {data_type}")



