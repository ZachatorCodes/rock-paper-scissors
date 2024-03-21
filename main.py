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

#Write your code below this line 👇
import random

option_images = [rock, paper, scissors]
option_text = ["rock", "paper", "scissors"]

print("Welcome to the Rock, Paper, Scissors game!")
print(rock, paper, scissors)
print("This game has been sponsored by Bunk, the Fattest Cat West of the Mississippi.\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
opponent_choice = random.randint(0, 2)

print(f"\nYou chose: {option_text[user_choice]}")
print(option_images[user_choice])
print(f"Opponent chose: {option_text[opponent_choice]}")
print(option_images[opponent_choice])

if user_choice < 0 or user_choice > 2:
  print("Input not recognized. Goodbye!")
elif user_choice == opponent_choice:
  print("Tie game!")
elif user_choice == 0 and opponent_choice == 2:
  print("You win!")
elif user_choice == 1 and opponent_choice == 0:
  print("You win!")
elif user_choice == 2 and opponent_choice == 1:
  print("You win!")
else:
  print("You lose!")