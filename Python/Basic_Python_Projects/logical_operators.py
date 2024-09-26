print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You landed on the mystery island you want to venture into jungle or go along shore?"
                 " type J for jungle or S for shore. ")
if choice_1 == "J":
    choice_2 = input("You venture into jungle and found a "
                     "shiny cave do you want to go inside? Y for yes N for no. ")
    if choice_2 == "Y":
        print("You fell into a hole, end of the story.")
    elif choice_2 == "N":
        choice_3 = input("You came across a big temple with 3 doors witch door:"
                         " blue, red and green. Witch door do you choose type B for blue,"
                         " R for red and G for green")
        if choice_3 == "R":
            print("inside was a dragon!!!")
        elif choice_3 == "B":
            print("That was a trap, end of the story.")
        elif choice_3 == "G":
            print("goood job you found the treasure! You win.")





else:
    print("When you scouting through the shore a big shark jump"
          " out of the water and ate you thats end of the story. ")

