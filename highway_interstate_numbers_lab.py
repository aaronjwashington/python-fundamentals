highway_number = int(input())

# 1. Is it a primary or an auxilary highway
# 2. If it's an auxilary highway, which primary highway does it server?
# 3. Whether the primary (if applicable) what direction does it run north/south or east/west

# output if the highway is invalid Get and check input

if ((highway_number < 1) or (highway_number > 999) or ((highway_number % 100) == 0)):
    print(f"{highway_number} is not a valid interstate highway number.")
else: #valid
    if(highway_number > 99): #auxilary
        print(f"I-{highway_number} is auxiliary", end='')
        #get the primary     
        primary_number = highway_number % 100 #get the right most 2 digits
        print(f", serving I-{primary_number}", end='')
    else: #must be 1-99
       primary_number = highway_number
       print(f"I-{primary_number} is primary", end= '')
    if ((primary_number % 2) == 0):
        print(f", going east/west.")
    else: #odd
        print(f", going north/south.")
        