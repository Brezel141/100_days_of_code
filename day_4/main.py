#Rock, paper, scissors

import random

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

rps = [rock, paper, scissors]
random_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f'You chose{rps[user_choice]}')
print(f'Computer chose{rps[random_choice]}')

if user_choice == random_choice:
    print("It's a draw")
elif user_choice == 0 and random_choice == 1:
    print("You lost")
elif user_choice == 1 and random_choice == 2:
    print("You lost")
elif user_choice == 2 and random_choice == 0:
    print("You lost")
else:
    print("You win")