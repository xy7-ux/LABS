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

game_images = [rock, paper, scissors]

user_choice = int(input("Welcome in the game choose 0 for rock, 1 for paper, 2 for scissors "))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[user_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed wrong number. You loseee")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("its a draw")







# if user_choice == 1 and computer_choice == 0:
#     print(f"Computer choice {computer_choice}")
# elif user_choice == 1 and computer_choice == 1:
#     print("play again you both choose paper")
# elif user_choice == 1 and computer_choice == 2:
#     print("you loose")
# else:
#     print("you typed wrong number.")
#
# if user_choice == 0 and computer_choice == 0:
#     print("play again you both choose rock")
# elif user_choice == 0 and computer_choice == 1:
#     print("you loose")
# elif user_choice == 0 and computer_choice == 2:
#     print("you win")
# else:
#     print("you typed wrong number.")
#
#
# if user_choice == 2 and computer_choice == 0:
#     print("you loose")
# elif user_choice == 2 and computer_choice == 1:
#     print("you win")
# elif user_choice == 2 and computer_choice == 2:
#     print("play again you both choose sccisors")
# else:
#     print("you typed wrong number.")
#     # computer_choice = random.randint(0, 2)
#     # if computer_choice == 0:
#     # print("computer choose rock")
#     # elif computer_choice == 1:
#     # print("computer choose paper")
#     # else:
#     # print("computer choose scissors")

