import random
#rock 0, paper 1, scissors 2

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

user_choice = int(input("Welcome in the game choose 0 for rock, 1 for paper, 2 for scissors "))
computer_choice = random.randint(0, 2)
if user_choice == 1 and computer_choice == 0:
    print("your choice"
          '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
          "computer choice: "
'''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
          "you win")
elif user_choice == 1 and computer_choice == 1:
    print("play again you both choose paper")
elif user_choice == 1 and computer_choice == 2:
    print("you loose")


if user_choice == 0 and computer_choice == 0:
    print("play again you both choose rock")
elif user_choice == 0 and computer_choice == 1:
    print("you loose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")


if user_choice == 2 and computer_choice == 0:
    print("you loose")
elif user_choice == 2 and computer_choice == 1:
    print("you win")
elif user_choice == 2 and computer_choice == 2:
    print("play again you both choose sccisors")

    # computer_choice = random.randint(0, 2)
    # if computer_choice == 0:
    # print("computer choose rock")
    # elif computer_choice == 1:
    # print("computer choose paper")
    # else:
    # print("computer choose scissors")

