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


options = [ rock, paper, scissors]
choice = (input("What do you choose? Type 'rock', 'paper' or 'scissors'.\n")).lower()
computer_choice = random.choice(options)

if choice == "rock":
    print(rock)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice == paper:
        print("YOU LOSE!")
    elif computer_choice == rock:
        print("It's a draw.")
    else:
        print("YOU WIN!")
elif choice == "paper":
    print(paper)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice == paper:
        print("It's a draw.")
    elif computer_choice == rock:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif choice == "scissors":
    print(scissors)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice == paper:
        print("YOU WIN!")
    elif computer_choice == rock:
        print("YOU LOSE!")
    else:
        print("It's a draw.")

else:
    print("Invalid Input")
