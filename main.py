import random 

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct! You guessed the number!")