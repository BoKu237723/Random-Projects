print("Welcome to my Quiz Game!")

def startPlaying():
    
    data = {
        "What does CPU stands for?":"central processing unit",
        "What does GPU stands for?":"graphics  processing unit",
        "What does RAM stands for?":"random access memory",
        "What does AMP stands for?":"asymmetric multiprocessing",
        "What does SMP stands for?":"symmetric multiprocessing",
        "What does ISR stands for?":"interrupt service routine",
        "What does RBAC stands for?":"role-based access control"
    }

    correct = 0
    skip = 0

    for question, correct_answer in data.items():
        attempts = 0
        
        while True:
            if attempts < 2:
                answer = input(f"{question}\nYour Input: ")
                attempts += 1
                if answer.lower() == correct_answer:
                    print("Correct!")
                    correct += 1
                    break
                elif answer.lower() == "skip":
                    print("Skipped!")
                    skip += 1
                    break
                else:
                    print("Incorrect!")
            else:
                print("Maximul Attempts exceeded! Going to next question!")
                print(f"Total Attempts for this question: {attempts}")
                break
        
    print(f"\nYou got {correct} out of {len(data)}. You got {(correct/len(data)*100):.2f}% of all quizes!")
    

def main():
    print("____ GAME RULES ____\n")
    print("- Only 2 attempts for each question")
    print("- Type 'skip' to skip the question (this will count as incorrect)")
    print("\n")

    while True:
        playing = input("Do you want to play?\nYour input: ")

        if playing.lower() in ['yes', 'y']:
            print("Okay! Let's play =)")
            startPlaying()
            break

        elif playing.lower() in ['no', 'n']:
            print("bye bye!")
            break
        else:
            print("Wrong input! Try Again!")
            continue

if __name__ == "__main__":
    main()
