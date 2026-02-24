import random 

number = random.randint(1,100)
guess = 0
attempt = 0
while guess != number:
    guess = int(input("Enter a number between 1 and 100: "))
    attempt += 1
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print(f"Correct! You guessed the number in {attempt} attempts.")