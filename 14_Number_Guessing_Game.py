import random
secret = random.randint(1, 20)
guess = None
while guess != secret:
    guess = int(input("Guess the number (1–20): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Correct!")