import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct! 🎉")
        break
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")