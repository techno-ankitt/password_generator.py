import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    try:
        length = int(input("\nEnter password length : "))
        
        if length == 0:
            print("Exiting... Thank you!")
            break
        elif length < 4:
            print("Password length should be at least 4!")
        else:
            print("Your Random Password:", generate_password(length))
    
    except ValueError:
        print("Please enter a valid number!")
