import random

# Player chooses a number to use as the highest range
upper_range = input("Please type the number to use as the range: ")

# A number is generated between 0 and the players chosen number
if upper_range.isdigit():
	upper_range = int(upper_range)
	print(f"A random number between 0 and {upper_range} has been generated!")
	if upper_range <= 0:
		print("Please type a number greater than 0")
		quit()
else:
    print("Please type a number next time")
    quit()

randNum = random.randint(0, upper_range)
guesses = 0

# Track and log the guesses, whether 
# the guess is less than or more than 
# the actual number and the amount of guesses
while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    
    if user_guess == randNum:
        print(f"You got it, the number was {user_guess}!")
        break
    elif user_guess > randNum:
        print("Lower!")
    else:
        print("Higher!")
            
print(f"Congratulations, you got it in {guesses} tries!")