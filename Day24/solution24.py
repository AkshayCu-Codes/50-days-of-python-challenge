def average_calories():
    total = 0
    count = 0

    while True:
        entry = input("Enter calories (or 'done' to finish): ")
        
        if entry.lower() == 'done':
            break
        
        try:
            calories = float(entry)
            total += calories
            count += 1
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    if count == 0:
        print("No calorie entries provided.")
    else:
        average = total / count
        print(f"Average calorie intake: {average:.2f}")

if __name__ == "__main__":
    average_calories()
