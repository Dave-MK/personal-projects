print("Welcome to my Viking quiz!")

playing = input("Do you want to play? (y/n) ")

if playing != "y":
	quit()

print("Okay! Let's Play: ")

# Question 1
answer = input("Who is the Allfather? ").lower()

if answer == "odin":
	print("Correct!")
else:
    print("Incorrect!")

# Question 2
answer = input("Who was the god of thunder? ").lower()

if answer == "thor":
	print("Correct!")
else:
    print("Incorrect!")
    
# Question 3
answer = input("What is the name of Thors hammer? ").lower()

if answer == "mjolnir":
	print("Correct!")
else:
    print("Incorrect!")
    
# Question 4
answer = input("Who is the trickster? ").lower()

if answer == "loki":
	print("Correct!")
else:
    print("Incorrect!")