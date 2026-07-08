import random


def number_guessing():
    print("\n\n---Welcome to the Number Guessing Game!---")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    print("\n\nChoose difficulty level:\n1. Easy(10 chances)\n2. Medium(5 chances)\n3. Hard(3 chances)\n")

    difficulty = int(input("Enter your choice: "))

    if difficulty == 1:
        print("Great! You have selected the Easy difficulty level")
        print("Let's start the game!")
        chances = 10
    elif difficulty == 2:
        print("Great! You have selected the Medium difficulty level")
        print("Let's start the game!")
        chances = 5
    elif difficulty == 3:
        print("Great! You have selected the Hard difficulty level")
        print("Let's start the game!")
        chances = 3
    else:
        print("Please choose a valid difficulty")

    random_number = random.randint(1,100)

    def guess_chances():

        attempts = 0

        while attempts < chances:
            attempts += 1
            user_guess = int(input("Enter your guess: "))
            if user_guess == random_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif user_guess > 100:
                print("The Number is b/w 1 & 100")
            elif attempts == chances:
                print(f"You run out of chances the number was {random_number}")
            else:
                if user_guess > random_number:
                    print(f"Incorrect! The number is less than {user_guess}.")
                elif user_guess < random_number:
                    print(f"Incorrect! The number is greater than {user_guess}.")
    
    guess_chances()
        

number_guessing()