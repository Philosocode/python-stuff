# This is a "guess the number" game.
import random
secretNumber = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

# Ask the player to guess 15 times.
for guessesTaken in range(
        1,
        16):  # Generate new global VAR: 'guessesTaken' and FOR Loop 10 times.
    print("Take a guess.")
    guess = int(input())  # Get the user's guess.

    # If guess is too high or too low, display message.
    # Else if guess is correct, break.
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

# If guess is correct, display this message.
# NOTE - 'guessesTaken' is not a local VAR. It's a global VAR.
if guess == secretNumber:
    print("You got it! You guessed my number in " + str(guessesTaken) +
          " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
