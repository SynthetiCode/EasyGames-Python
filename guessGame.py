#This is a "Guess the number game"

import random
print('Hello. What is your nombre?')
nombre = input()
print('Well, ' + nombre + ', I am thining of a numero between Uno(1) y Veinte(20)')
secretNumber =random.randint(1,20)

#ask player 6 times
for guessesTaken in range(0, 6):
	print ('Take a guess:' )
	guess = int(input())
	if guess < secretNumber:
		print ('Your guess is too low.')
	elif guess > secretNumber:
		print ('Your guess is too high.')
	else:
		break # <-- This condition is the correct guess!
if guess ==secretNumber:
	print ('Good job, ' + nombre + '! You guessed my number in ' + str(guessesTaken+1)+ ' guesses!')
else:
	print ('Nope, the number I was thinking of was: ' + str(secretNumber))
	print ('Better luck next time')


