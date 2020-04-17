# this is the guess the number game
import random
print('hello . what is your name?')
name = input()
secretNumber = random.randint(1,20)
print('well,' + name + ',i am thinking of the number between 1-20')

# ask the player to guess 6 times,
for guessesTaken in range (1,7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your is too high')
    else:
        break

if guess == secretNumber:
    print('good job...!!!' + name + ' you guessed my number in  ' + str(guessesTaken) + ' guesses')

else:
    print('nope the number i was thinking was ' + str(secretNumber))
