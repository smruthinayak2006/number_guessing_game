import random

def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            return 1, 50, 10
        elif choice == '2':
            return 1, 100, 7
        elif choice == '3':
            return 1, 200, 5
        else:
            print("Invalid choice. Try again.")

def get_valid_guess(low, high):
    while True:
        try:
            guess = int(input(f"Enter a number between {low} and {high}: "))
            if low <= guess <= high:
                return guess
            else:
                print("Out of range! Try again.")
        except ValueError:
            print("Invalid input! Enter a number.")

def give_hint(number, guess):
    diff = abs(number - guess)

    if guess < number:
        direction = "Higher"
    else:
        direction = "Lower"

    if diff <= 5:
        print(f"{direction} (Very close!)")
    elif diff <= 10:
        print(f"{direction} (Close!)")
    else:
        print(f"{direction} (Far!)")

def play_game():
    low, high, max_attempts = choose_difficulty()
    number = random.randint(low, high)
    attempt = 0

    print("\nGame Started!")

    while attempt < max_attempts:
        guess = get_valid_guess(low, high)
        attempt += 1

        if guess == number:
            score = max_attempts - attempt + 1
            print(f"\n🎉 Correct! You guessed it in {attempt} attempts.")
            print(f"Your Score: {score}")
            return
        else:
            give_hint(number, guess)
            print(f"Attempts left: {max_attempts - attempt}")

    print(f"\nGame Over! The number was {number}")

def main():
    print("Welcome to Number Guessing Game!")

    while True:
        play_game()
        choice = input("\nPlay again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()