#Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184

#Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

#Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output calories burned for women and men.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print('Men: {:.2f} calories'.format(calories_man))


age_years= float(input())

weight_lbs = float(input())

heart_rate = float(input())

time_min = float(input())


women_calories = ((age_years * 0.074) - (weight_lbs * 0.05741) + (heart_rate * 0.4472) - 20.4022) * (time_min / 4.184)

men_calories = ((age_years * 0.2017) + (weight_lbs * 0.09036) + (heart_rate * 0.6309) - 55.0969) * (time_min / 4.184)



print('Women: {:.2f} calories'.format(women_calories))

print('Men: {:.2f} calories'.format(men_calories))

