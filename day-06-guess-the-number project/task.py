import random
secret_number = random.randint(1,20)
guess = int(input("Pick a number between 1-20 \n"))
while guess != secret_number:
    difference = abs(guess - secret_number)
    if guess > secret_number:
        if difference >= 10:
            print("Too High!")
        elif difference >= 5:
            print("Quite High!")
        else:
            print("You're close!")
    elif guess < secret_number:
        if difference >= 10:
            print("Too Low!")
        elif difference >= 5:
            print("Quite Low!")
        else:
            print("You're close!")
    guess = int(input("Guess the number again\n"))

print("You got it!")
