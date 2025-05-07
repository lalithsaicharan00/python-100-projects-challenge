import random

secretNumber = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

print("i will give you hints if you are too high or too low.")

print("let's see if you can guess it!")

guess = 0

while guess != secretNumber:
    guess = int(input("Take a guess: "))

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You guessed the number {secretNumber} correctly!")
        break

print("Thanks for playing!")

