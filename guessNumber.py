import random

# Generate a random number between 0 and 100
secret_number = random.randint(0, 100)

# Initialize the number of attempts
attempts = 0

# Main game loop
while True:
    try:
        # Get user's guess
        guess = int(input("Guess the number between 0 and 100: "))

        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid integer between 0 and 100.")