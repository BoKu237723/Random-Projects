import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_cretria = False
    has_number = False
    has_special = False

    while not meets_cretria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_cretria = True
        if numbers:
            meets_cretria = has_number
        if special_characters:
            meets_cretria = meets_cretria and has_special

    return pwd

min_length = int(input("Enter the minimul length: "))
has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you want to have special_characters (y/n)?").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print(f"Generatedd password is {pwd}")
















