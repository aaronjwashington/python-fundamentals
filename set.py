#Creating sets using set()

nums1 = set([1, 2, 3])

# Create a set using a set literal

nums2 = {4, 5, 6}

#print the contents of the sets

print(nums1)
print(nums2)

# Initial list contains some duplicate values

first_names = ['Alba','Hema','Ron','Alba','Musa','Ron','Ron']

#Creating a set removes duplicates

names_set = set(first_names)

#printing first names

print(names_set)



#Create sets

names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

#Add element to set

names1.add('Hyungu')

#Add names2 to names1

names1.update(names2)

# Remove element from set
names1.remove('Dean')

# Clear all elements from set
names2.clear()


# Create Sets using Set Theory

names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

# Union names1 and names2

result_set = names1.union(names2)

# Intersection btwn result_set and names3

result_set = result_set.intersection(names3)

# Difference btwn result_set and names4

result_set = result_set.difference(names4)

# Names

male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

all_names = male_names.union(female_names)

neutral_names = male_names.intersection(female_names)

specific_names = all_names.difference(neutral_names)


print(sorted(all_names))
print(sorted(neutral_names))
print(sorted(specific_names))



