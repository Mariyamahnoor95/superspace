# this is the guess the number game
import random
print('Hello! What is your name?')
name = input()
secretNumber = random.randint(1,20)
print('Well,' + name + ',I am thinking of the number between 1-20')

# ask the player to guess 6 times,
for guessesTaken in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job...!!! ' + name + 'you guessed my number in  ' + str(guessesTaken) + ' guesses')
    print('Thanks')

else:
    print('Nope the number I was thinking was ' + str(secretNumber))
    print('Try Again!')
