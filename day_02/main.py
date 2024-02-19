# Tip calculator

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