#rock pape scissor
import random
def user():
    while True:
        user=input("Enter Rock, Paper or  Scissors:").lower()
        if user in ['rock','paper','scissors']:
            return user
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def computer():
    choices=['rock','paper','scissors']
    return random.choice(choices)

def determinewinner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a Tie"
    elif (user_choice=='rock'and computer_choice=='scissors') or \
         (user_choice=='paper'and computer_choice=='rock')or \
         (user_choice=='scissors'and computer_choice=='paper'):
        return "You Win"
    else:
        return "Computer Win"
    
def playgame():
    print("Let's Play Rock Paper and Scissors!")
    while True:
        user_choice=user()
        computer_choice=computer()
        print(f"You choose {user_choice.upper()}.")
        print(f"Computer choose {computer_choice.upper()}.")
        result=determinewinner(user_choice,computer_choice)
        print(result)
        play_again=input("Do you Want to play again? (y/n)").lower()
        if play_again!='y':
            break
        elif play_again=='n':
            print("Thank you for Playing")

playgame()