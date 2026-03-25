import random

attempts = 0

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")


number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess < number:
        print("Too low.")

    elif guess > number:
        print("Too high.")

    else:
        print(f"You guessed right in {attempts} attempts.!")
        break





