print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay,lets play!!")
score = 0

answer = input("What does URL stands for ? ")
if answer.lower() == "uniform resource locator":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RAM stands for ? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input("What does CEO stands for ? ")
if answer.lower() == "chief executive officer":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input("What does ATM stands for ? ")
if answer.lower() == "automated teller machine":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input("What does GPS stands for ? ")
if answer.lower() == "global positioning system":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input("What does PIN stands for ? ")
if answer.lower() == "personal identification number":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")


print("Your score is - > " + str(score));
print("Thank you!")