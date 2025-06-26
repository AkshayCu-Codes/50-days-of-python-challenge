from datetime import datetime

def age_in_minutes():
    current_year = datetime.now().year

    while True:
        birth_year = input("Enter your Birth Year (4 digits):").strip()

        if not birth_year.isdigit() or len(birth_year) != 4:
            print("Enter a valid 4-digit birth year.")
            continue

        birth_year = int(birth_year)

        if birth_year < 1900 or birth_year > current_year:
            print(f"Enter your birth year between 1900 and {current_year}.")
            continue

        break

    age = current_year - birth_year
    age_min = age * 365 * 24 * 60

    print(f"You are {age_min:,} minutes old.")

age_in_minutes()


# output
# Enter your Birth Year (4 digits):2000
# You are 13,140,000 minutes old.