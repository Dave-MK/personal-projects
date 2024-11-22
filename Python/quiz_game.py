print("Welcome to my Viking quiz!")

playing = input("Do you want to play? (y/n) ")

if playing != "y":
	quit()

print("Okay! Let's Play: ")

score = 0

# Question 1
answer = input("Who is the Allfather? ")

if answer.lower() == "odin":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Who was the god of thunder? ")

if answer.lower() == "thor":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")
    
# Question 3
answer = input("What is the name of Thors hammer? ")

if answer.lower() == "mjolnir":
		print("Correct!")
		score += 1
else:
    print("Incorrect!")
    
# Question 4
answer = input("Who is the trickster? ")

if answer.lower() == "loki":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")

cent = (score / 4) * 100

print(f"You got {str(score)} questions correct!")
print(f"Meaning you got {str(cent)}% of the questions correct!")