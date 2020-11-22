from hangman_art import logo
from hangman_words import word_list
import random

# Day 1 - Band Name Generator

print("Welcome to the 'Band Name Generator'")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet that you've owned?\n")
print("Your band name is " + city + " " + pet)

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
                print('''   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||''')
                print(
                    "The coachman knows where the treasure is and will take you there.")
                print("Congradulations, you've won the game.")
            else:
                print("You've been struck by lightning. Game over.")
    else:
        print("You have been eaten by a shark. Game over")
        print('''

                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|''')
else:
    print("You've fallen in a hole. Game over.")

# Day 4
# Practice Exercise - Treasure Map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"
# Another option:
# map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Rock - Paper - Scissors (random.choice)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures = [rock, paper, scissors]
choice = input("Do you choose 'rock', 'paper', or 'scissors'? \n")
randomize = random.choice(gestures)

if choice == "rock":
    print(rock)
    print(randomize)
elif choice == "paper":
    print(paper)
    print(randomize)
else:
    print(scissors)
    print(randomize)

# Rock - Paper - Scissors (random.randint)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
print(gestures[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(gestures[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("Computer wins!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("Computer wins!")
elif computer_choice == user_choice:
    print("It's a draw")

# Day 5
# Practice Exercise - Average student height in a class
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights = int(student_heights[n])
# print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

avg_height = round(total_height/number_of_students)
print(avg_height)

# Practice Exercise - Fizzbuzz Job Interview Question

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

for char in password_list:
    password += char

print(f"Your password is: {password}")

# Day 6
# https://reeborg.ca/index_en.html
# Hurdle 3


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Hurdle 4


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if wall_in_front:
        jump()
    else:
        move()

# Maze


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Day 7 - Hangman
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])
