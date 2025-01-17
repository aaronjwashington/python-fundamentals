user_channel = int(input())
   
if (user_channel >= 2) and (user_channel <= 499):
    channel_type = 's'

elif (user_channel >= 1002) and (user_channel <= 1499):
    channel_type = 'h'

else:
    channel_type = 'e'

print('Channel type:', channel_type)



# Explicit defined ranges

if x < 0 :
    # Negative

elif  (x >= 0) and (x <= 10) :
    # 0..10

elif  (x >= 11) and (x <= 20) :
    # 11..20

else :
    # 21+



# Implicit Defined Ranges

if x < 0 :
  # Negative

elif (x <= 10) :
  # 0..10

elif (x <= 20) :
  # 11..20

else :
  # 21+
  
  
  
# Dectect Number Range

user_age = int(input())

if user_age >= 18 and user_age <= 25:
    print('Eligible')
else:
    print('Ineligible')
