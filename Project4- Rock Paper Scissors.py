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

game_images=[rock,paper,scissors]

#Ask the user about His choice
user_choice = int(input("What do you choose? Press 0 for Rock , 1 for Paper or 2 for Scissors. \n"))
print(game_images[user_choice])

computer_choice = random.randint(a=0 , b =2)
print("computer choose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You Typed an Invalid Number.You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice > user_choice :
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a Draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif user_choice > computer_choice :
    print("You Win!")
