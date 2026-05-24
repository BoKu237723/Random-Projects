name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?\nYour Input: ").lower()

if answer == "left":
    answer = input("\nYou come to a river, and you can walk around it or swim across? Wich way would you like to go?\n Your Input: ").lower()
    if answer == "walk":
        print("\nYou walked for many miles, ran out of water and you fell to the ground")
    elif answer == "swim":
        print("\nYou swan across and were eaten by a bear")
    else:
        print("Not a valid option")
elif answer == "right":
    answer = input("\nYou come to a bridge, it looks wobbly, do you want to cross it or head back?\nYour Input: ")
    if answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them?\nYour Input: ")
        if answer == "yes":
            print("\nYou talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("\nYou ignored the stranger and they are offended and you lose =)")
            pass
        else:
            print("Not a valid option.")
            
    elif answer == "back":
        print("\nYou go back and lose =)")
    else:
        print("Not a valid option.")
else:
    print("Not a valid option.")
























