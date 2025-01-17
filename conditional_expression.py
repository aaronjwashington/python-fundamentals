#Create a conditional expression that evaluates to string "negative" if user_val is less than 0, and "non-negative" otherwise.

user_val = int(input())

cond_str = 'negative' if (user_val < 0) else 'non-negative'

print(user_val, 'is', cond_str)



# Using a conditional expression, write a statement that increments num_users if update_direction is 3, otherwise decrements num_users.

num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users - 1

print('New value is:', num_users)