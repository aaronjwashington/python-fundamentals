# Write a program with two inputs, current price and last month's price (both integers).
# Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

current_price = int(input())
last_months_price = int(input())

price_diff = current_price - last_months_price
mortgage = (current_price * 0.051) / 12

print(f"This house is ${current_price}. The change is ${price_diff} since last month.")

print(f"The estimated monthly mortgage is ${mortgage:.2f}.")