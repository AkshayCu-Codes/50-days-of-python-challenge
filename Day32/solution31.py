def password_validator():
    while True:
        password = input("Enter password: ")
        errors = []

        # Check for minimum length
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")

        # Check for at least one uppercase
        if not any(char.isupper() for char in password):
            errors.append("Password must contain at least one uppercase letter")

        # Check for at least one lowercase
        if not any(char.islower() for char in password):
            errors.append("Password must contain at least one lowercase letter")

        # Check for at least one digit
        if not any(char.isdigit() for char in password):
            errors.append("Password must contain at least one digit")

        # If no errors, break loop
        if not errors:
            print("Password is valid!")
            return password
        else:
            for err in errors:
                print(f"Error: {err}")


password_validator()