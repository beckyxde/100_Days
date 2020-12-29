from gestures import rock, paper, scissors

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