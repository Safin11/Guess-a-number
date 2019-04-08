import random
g = int(input("Guess a number from 1 to 10!"))
if g == random.randint(1, 10):
    print("You've guessed it!")
    input()
else:
    n = int(input("Give it another try, guess again!"))
    if n == random.randint(1, 10):
        print("You've guessed it!")
    else:
        print("Sorry, that was your last chance. You have lost, press Enter to exit game.")
        input()
