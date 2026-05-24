import random

def main():
    random_number = random.randint(0,11)
    attempts = 0
    print("___ Guess a Number between 0 - 11\n")
    while True:
        try:
            guess = input("Enter your number: ")
            guess = int(guess)
            attempts += 1
            if guess < 0:
                print("Don't type a number smaller than 0")
                continue

            if guess == random_number:
                print("Correct!")
                print(f"Random Generated Number: {random_number}")
                print(f"Total attempts: {attempts}")
                break
            else:
                if guess < random_number:
                    print("Guess Larger!\n")
                else:
                    print("Guess Smaller!\n")
                continue
        except ValueError:
            print("This is not an integer!")
            continue    

if __name__ == "__main__":
    main()