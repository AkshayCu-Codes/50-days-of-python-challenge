import random

def user_name():
    name=input("Enter your name: ")

    rev_name=name[::-1]
    random_digit=str(random.randint(0,9))
    username=rev_name + random_digit

    print(username)

user_name()