# Project-4 = Rock, Paper, Scissors
import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_image=[rock,paper,scissors]
user_choice=int(input("What do you Choose? 0 for rock, 1 for paper, 2 for scissors. "))

if  user_choice>=3 or user_choice<0:
    print("You typed an Invalid Number. You Lose!")
else:
    print("You Choose-")
    print(game_image[user_choice])
    computer_choice=random.randint(0,2)
    print("\nComputer Choose-")
    print(game_image[computer_choice])
    print("\n")
    
    if user_choice==computer_choice:
        print("It's a Draw!\n")
    elif user_choice==0 and computer_choice==2:
        print("You Win!\n")
    elif computer_choice==0 and user_choice==2:
        print("You Lose!\n")
    elif computer_choice>user_choice:
        print("You Lose!\n")
    elif user_choice>computer_choice:
        print("You Win!\n")
    else:
        print("Thank you for visiting!")

