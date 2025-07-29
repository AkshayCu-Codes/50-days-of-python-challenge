def save_emails():
    while True:
        email= input("\nEnter your email address (type 'done' to finish):")
        if email.lower() == 'done':
            break
        with open("emails.csv", "a") as file:
            file.write(email + "\n")
        print(f"Email '{email}' saved successfully.")

def open_emails():
    try:
        with open("emails.csv", "r") as file:
            emails = file.readlines()
            if emails:
                print("Saved Emails:")
                for email in emails:
                    print(email.strip())
            else:
                print("No emails saved yet.")
    except FileNotFoundError:
        print("No emails saved yet.")

def main():
    while True:
        print("\nEmail Management System")
        print("1. Save Email")
        print("2. Open Emails")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            save_emails()
        elif choice == '2':
            open_emails()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

        