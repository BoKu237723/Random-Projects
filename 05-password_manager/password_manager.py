from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as kf:
        kf.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"\nUser: {user} \nPassword: {fer.decrypt(passw.encode())}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()}\n")
    
    f.close()

while True:
    mode = input("\nWould you like to add a new password or view existing ones? (view, add, q to quit)\nYour Input: ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode in ["q", "quit"]:
        print("\nBye Bye!")
        quit()
    else:
        print("Invalid Mode")
        continue
