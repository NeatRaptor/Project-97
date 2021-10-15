import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 and 9): ")

while chances < 5:
    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Congratulations, you won")
    elif guess > number:
        print("Your guess was too high, guess a number lower than ", guess)
    else:
        print("Your guess was too low, Guess higher than ", guess)

    chances=+1

if not (chances < 5):
    print("You lose, the number is ", number)