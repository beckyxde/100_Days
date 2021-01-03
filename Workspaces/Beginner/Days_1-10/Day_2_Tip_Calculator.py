import math

# Day 2
# Practice Exercise - Remaining Life Calculator
age = input("What is your current age?")
remaining = 90 - int(age)
days = 365 * remaining
weeks = 52 * remaining
months = 12 * remaining
message = f"You have {days} days, {weeks} weeks, and {months} months left"
print(message)

# Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip/100
total_tip = bill * tip_as_percentage
total_bill = bill + total_tip
per_person = total_bill/people
total_amount = round(per_person, 2)
message = f"Each person should pay: ${total_amount}"
print(message)