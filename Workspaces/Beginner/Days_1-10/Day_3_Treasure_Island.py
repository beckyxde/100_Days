import math
from treasure_island import shark, treasure

# Day 3
# Practice Exercise - Leap Year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")

# Practice Exercise - Pizza Order
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"You final bill is ${bill}")

# Practice Exercise - Love Compatibility calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

print(f"You two are {score}% compatible")

if score > 10 or score < 90:
    print(f"Your score is {score}%; You two go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}%; You two are alright together")
else:
    print(f"Your score is {score}")

# Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Chose a direction: left or right\n")

if direction == "left":
    lake = input("You have reached a lake. Do you want to swim or wait?\n")
    if lake == "wait":
        helicoptor = input(
            "A helicopter is approaching. Do you want to get inside? Yes or No\n")
        if helicoptor == "yes":
            print("The helicopter crashes. Game over")
        else:
            horse = input(
                "A horse draw carriage arrives. Do you want to 'get inside' or 'stay put'?\n")
            if horse == "get inside":
                print(treasure)
                print(
                    "The coachman knows where the treasure is and will take you there.")
                print("Congradulations, you've won the game.")
            else:
                print("You've been struck by lightning. Game over.")
    else:
        print("You have been eaten by a shark. Game over")
        print(shark)
else:
    print("You've fallen in a hole. Game over.")