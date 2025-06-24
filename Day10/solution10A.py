def hide_password():
    password=input("Enter the passwrd ")
    hidden='*' * len(password)
    print(hidden)
    print(f'your password is {len(password)} character long.')

hide_password()