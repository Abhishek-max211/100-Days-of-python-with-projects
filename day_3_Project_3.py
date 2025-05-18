# Project-3 = Treasure Island
print('''**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your Mission is to find the Treasure!")

direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    lakechoice = input('You have come to a lake. There is an island in the middle of the lake.'
                       ' Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if lakechoice == "wait":
        choice1 = input('You arrive at the island unharmed.'
                        ' There is a house with 3 doors. '
                        'One red, one yellow, and one blue. Which color do you choose? ').lower()
        if choice1 == "red":
            print("It is a room full of fire. Game Over!")
        elif choice1 == "yellow":
            print("You found the treasure. You Win!")
        elif choice1 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("Invalid Input!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")