#Wap to play rock paper and scissors.
import random

def userchoice():
    while True:
        userchoice = input("Enter Rock, Paper, or Scissors: ").lower()
        if userchoice in ['rock', 'paper', 'scissors']:
            return userchoice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def computerchoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determinewinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def playgame():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = userchoice()
        computer_choice = computerchoice()

        print(f"You chose {user_choice.upper()}.")
        print(f"The computer chose {computer_choice.upper()}.")

        result = determinewinner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

playgame()