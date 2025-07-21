import random
import string

def generate_password():
    strength = input("How strong do you want your password? (weak/w, strong/s, very strong/vs): ").lower()

    if strength in ["weak", "w"]:
        length = 5
    elif strength in ["strong", "s"]:
        length = 8
    elif strength in ["very strong", "vs", "verystrong"]:
        length = 12
    else:
        print("Invalid input. Choose from: weak/w, strong/s, or very strong/vs.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)
    return password

generate_password()
