#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_float = float(total)
tip_float = float(tip)
people_float = float(people)

tip_percent = tip_float / 100
tip_total = total_float * tip_percent
total_plus_tip = total_float + tip_total
total_per_person = total_plus_tip / people_float
total_per_person_rounded = round(total_per_person, 2)

print(f"Each person should pay: ${total_per_person_rounded}")