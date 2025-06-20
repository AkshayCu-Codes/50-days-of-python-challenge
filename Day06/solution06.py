def user_name():
    email=input("Enter your Email: ")
    username=email.split('@')[0]
    return username

print('Username : '+ user_name())

# output

# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge\Day06> python solution06.py
# Enter your Email: akshay@gmail.com
# Username : akshay
# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge\Day06> python solution06.py
# Enter your Email: Samir1234@gmail.com
# Username : Samir1234