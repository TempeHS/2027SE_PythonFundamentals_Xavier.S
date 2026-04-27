import random

# getting the range from the person
while True:
    try:
        number = int(input("Number? "))
        if number > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("That is not an integer. Try again.")

    # Randomizing the number
secret = random.randint(1, number)

while True:
    try:
        guess = int(input("Guess"))
        if guess == secret:
            print("correct")
            break
        elif guess > secret:
            print("lower")
        else:
            print("Higher")
    except ValueError:

        pass


# Prompting the user to guess the number
