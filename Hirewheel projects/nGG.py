#Randomly select a number between 1 and 100 when the game starts.
import random
correct_number = random.randint(1,100)
#Prompt the user for guesses until they find the number.

while True:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        #Tell the user whether their guess is too high or too low, and allow repeated attempts.
        if user_guess > correct_number:
            print("Too high! Try again.")
        elif user_guess < correct_number:
            print("Too low! Try again.")
        #Congratulate the player and exit when the guess is correct.
        else:
            print("Congratulations! You guessed the number correctly.")
            break
        #Handle invalid inputs gracefully (non-numeric values or numbers outside the range).
    except ValueError:
        print("Invalid input. Please enter a valid number.")
