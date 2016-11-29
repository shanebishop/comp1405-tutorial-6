#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Imports
from random import *

# Variable to store the random number
random_int = -1

# Variable to store the number of guesses made by the user
num_guesses = 0

# Initializes a new game
def new_game():
	# Lets Python know I want to change the values of the global variables
	global random_int
	global num_guesses
	
	# Intialize the random number to a number in [1, 100]
	random_int = randint(1, 100)
	
	# Intialize number of guesses to 0 (required for games after first game)
	num_guesses = 0

def main():
	# Lets Python know I want to change the value of num_guesses
	global num_guesses
	
	# Make a new game
	new_game()
	
	# Variable to see if the user wishes to continue playing
	keep_going  = "Y"
	
	while keep_going == "Y":
		# Asks the user for a new guess and increments num_guesses
		num_entered = int(input("Please input a geuss: "))
		num_guesses += 1
		
		# If the user guessed correctly ...
		if num_entered == random_int:
			# ... congradulate user ...
			print("Congratulations! You won! (It only took you", num_guesses, "guesses.)")
			
			# ... and then start a new game if the user wishes
			if input("Would you like to play again? ('Y' or 'N') ").upper() == "Y":
				new_game()
				continue
			else:
				break
		# User guessed too high
		elif num_entered > random_int:
			print("Your geuss was too HIGH")
		# User guessed too low
		else:
			print("Your geuss was too LOW")

# Start execution of program
main()