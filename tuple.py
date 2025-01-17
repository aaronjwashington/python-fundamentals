#Using Tuples

white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

# Error. Tuples are immutable
#white_house_coordinates[1] = 50


#Named Tuples

from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats']) #create the named tuple

chevy_blazer = Car('Chevrolet','Blazer',32000 ,275 ,8) #Use the named tuple to describe a car

chevy_impala = Car('Chevrolet','Impala',37495 ,305 ,5) #Use the named tuple to describe a different car

print (chevy_blazer)

print (chevy_impala)

print ('')

# Creating a named tuple

Player = namedtuple('Player',['name', 'number', 'position' ,'team'])

cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')

print(cam.name + '(#' + cam.number + ')' + ' is a ' + cam.position + ' for the ' + cam.team + '.')
print(lebron.name + '(#' + lebron.number + ')' + ' is a ' + lebron.position + ' for the ' + lebron.team + '.')
