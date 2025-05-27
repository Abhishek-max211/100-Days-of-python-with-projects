# Project-12 = The Number Guessing Game
from random import randint

print('''

░██████╗░██╗░░░██╗███████╗░██████╗░██████╗ ████████╗██╗░░██╗███████╗
██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝
██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░
██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░
╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗
░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')
easy_turns=10
hard_turns=5
turns=0

def check_answer(user_guess,actual_answer,turns):
    """Checks answer against guess, returns the number of terms remaining."""
    if user_guess>actual_answer:
        print("Too High.")
        return turns-1
    elif user_guess<actual_answer:
        print("Too Low.")
        return turns-1
    else:
        print(f"You got it. The answer was {actual_answer}")

def set_difficulty():
    level=input("choose the difficulty. Type 'easy' or 'hard': ").lower()
    if level=="easy":
       return easy_turns
    else:
        return hard_turns
    
def game():
    print("Welcome To The Number Guessing Game!")
    print("I am thinking a number between 1 and 100.")
    answer=randint(1,100)

    turns=set_difficulty()

    guess=0
    while guess !=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have run of guesses, you lose.")
            return
        elif guess!=answer:
            print("Guess Again.")
game()