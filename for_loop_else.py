"""
for name in iterable:
    # Loop body: Sub-statements to execute 
    # for each item in iterable
else:
    # Else body: Sub-statements to execute 
    # once when loop completes

# Statements to execute after the loop
"""
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end= ' ')
else:
    print('All names printed.')