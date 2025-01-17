#Looping over a sequence in reverse.

names = ['Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]


for name in names:
    print(name, '|', end='')
    
print('\n Printing in reverse:')
for name in reversed(names):
    print(name, '|', end='')