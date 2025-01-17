# Some of the most expensive cars in the world

lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]


print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

prices.append('Camary')
print('After append:', prices)


# Write a statement that assigns the 2nd element of my_towns with 'Detroit'.
# my_towns[1] = 'Detroit'

my_list = [10, 'bw']
print(my_list)

my_list.append('abc')
print('After append:', my_list)

my_list.pop(1)
print('After pop:', my_list)

my_list.remove('abc')
print('After remove:', my_list)


#Using sequence-type functions with lists.

house_prices = [380000, 900000, 875000] + [225000]

print('There are', len(house_prices), 'prices in the list.')

#Find min, max

print('Cheapest house:', min(house_prices))
print('Expensive house:', max(house_prices))


#Program to calculate statistics from student test scores.

midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(num_midterm_scores, 'students took the midterm.')
print(num_final_scores, 'students took the final.')

#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(dropped_students, 'students must have dropped the class.')

#Write an expression that concatenates the list feb_temps to the end of jan_temps.

jan_temps + feb_temps


#Write a statement that assigns the variable avg_price with the average of the elements of prices.

avg_price = sum(prices) / len(prices)