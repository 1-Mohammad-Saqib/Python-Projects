# Number Guessing Game
# Computer secretly chooses:
# secret = 7
# Ask the user repeatedly until they guess correctly.
# If the guess is wrong:
# Try Again
# If correct:
# Congratulations!
# Use:
# while
# break
print("=========Number Guess Game=========")
secret = 7
guess = int(input("Guess the number: "))

while True:
    if guess < 0:
        print("Please choose a positive number")
        guess = int(input("Enter the positive number: "))
    elif guess > secret + 30:
        print("Too large please choose smaller number")
        guess = int(input("Enter the number again: "))
    elif guess >= secret + 7:
        guess = int(input("Choose the smaller number : "))
    elif guess < secret:
        print("You are close to the secret choose a larger number ")
        guess = int(input("Enter the number again: "))

    elif guess > secret and guess < secret + 7 :
        print("You are close to the number choose a smaller number")
        guess = int(input("Enter the number again: "))

    elif guess == secret:
        print("Congratulations! You guessed the secret number.")
        break
