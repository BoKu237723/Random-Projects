import random
import datetime
from datetime import datetime

def record(location):
    now = datetime.now()
    with open ("record.txt", "a") as f:
        f.write(f"{now} : {location}\n")

def main():

    user_wins = 0
    computer_wins = 0
    
    available_list = ['rock', 'paper', 'scissors']

    while True:
        user_input = input("Type Rock/Paper/Scissors or 'q' to quit\nYour Input: ").lower()
        if user_input.lower() == "q":
            print(f"User Scores: {user_wins}")
            print(f"Computer Scores: {computer_wins}")
            quit()
    
        elif user_input in available_list:
            computer_item = random.choice(available_list)
            print(f"Computer choice: {computer_item}")
    
            if computer_item == user_input:
                print("Tie!\n")
                record("User and Computer were Tie")
    
            elif computer_item == 'rock' and user_input == 'scissors':
                print("You Lose!\n")
                computer_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Loses.")
            
            elif computer_item == 'rock' and user_input == 'paper':
                print("You Win!\n")
                user_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Wins.")
    
            elif computer_item == 'paper' and user_input == 'rock':
                print("You Lose!\n")
                computer_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Loses.")
    
            elif computer_item == 'paper' and user_input == 'scissors':
                print("You Win!\n")
                user_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Wins.")
    
            elif computer_item == 'scissors' and user_input == 'paper':
                print("You Lose!\n")
                computer_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Loses.")
    
            elif computer_item == 'scissors' and user_input == 'rock':
                print("You Win!\n")
                user_wins += 1
                record(f"User Chose {user_input} and Computer Chose {computer_item}. User Wins.")
    
        else:
            print("Invalid Input! Try again!")
            continue


if __name__ == "__main__":
    main()





























