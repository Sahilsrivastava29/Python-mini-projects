import random

top_of_range = input("Type a number")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
if top_of_range<= 0:
    print('Please type number greater than 0')
    quit()
else:
    print("Please type a digit")
    quit()

random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("Make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("Its Correct!")
        break
    else:
        print("You got it wrong")
