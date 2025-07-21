import random

def guess_a_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")

    while attempts < 3:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue  # Don't count invalid guesses as attempts

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 10.")
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_a_number()