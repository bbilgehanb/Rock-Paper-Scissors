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
Options = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
comp_choice=random.randint(0,2)
if user_choice<=2 and user_choice>=0:
  print(Options[user_choice])
  print(f"Computer chose:\n{Options[comp_choice]}")
  if user_choice == 0 and comp_choice == 2:
      print("You win!")
  elif comp_choice == 0 and user_choice == 2:
      print("You lose")
  elif comp_choice > user_choice:
      print("You lose")
  elif user_choice > comp_choice:
      print("You win!")
  elif comp_choice == user_choice:
      print("It's a draw")
else:
  print("You typed an invalid number. You lose!")

