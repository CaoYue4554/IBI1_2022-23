# What does this piece of code do?
# Answer: This code runs ten times and gives the largest random number from 1 to 100 in the 10 loops.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
# initialize figures for the two variables.
while progress<10:
	# This can only repeat 10 times.
	progress+=1
	# progress plus 1 and save the new figure as progress
	n = randint(1,100)
	# n varies from 1 to 100 randomly.
	if n > stored_random_number:
		stored_random_number = n
		# the stored_random_number will be larger in the loop.

print(stored_random_number)
#This prints the largest n number in the 10 loops.
