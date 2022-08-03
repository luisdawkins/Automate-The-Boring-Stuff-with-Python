#This is a guess the number game.
import random

print("Hello. What is your name?")
name = input()

print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
secretNumber = random.randint(1, 20)

#print("Debug: Secret number {}".format(str(secretNumber)))

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition for the correct guess!

if guess == secretNumber:
    print("Good job, {0}! You guessed my number in {1} guesses!".format(name,str(guessesTaken)))
else:
    print("Nope. The number I was thinking of was {0}".format(str(secretNumber) ))

print("You took {} guesses.".format(str(guessesTaken)) )