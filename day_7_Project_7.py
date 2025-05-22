import random

print("Welcome to the Hangman Game!")

stages = ['''
  +---+
  |   |
  O   |
 /|\\ |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["calm", "run", "apple", "banana"]
lives = 6  # Max index for stages is 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    guess = input("Guess the letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
    guessed_letters.append(guess)

    display = ""
    if guess in chosen_word:
        correct_letters.append(guess)
        print(f"Good guess: {guess}")
    else:
        lives -= 1
        print(f"You guessed '{guess}'. That's not in the word. You lose a life.")

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")

    if lives == 0:
        game_over = True
        print(f"You Lose! The word was '{chosen_word}'.")

    print(stages[lives])

print("\nThanks for visiting!")
