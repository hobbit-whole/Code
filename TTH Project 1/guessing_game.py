"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    #Psuedo-code
    
    print("Welcome to the Number Guessing Game!")
    answer = int(random.randrange(1,10))
    # 3. Continuously prompt the player for a guess.
    guess = 0
    attempt = 1
    
    while(guess != answer):
        
        
        
        try:
            guess = int(input("Pick a number (1-10): "))
            
            if (guess < 1 or guess > 10):
                print("Sorry guess is not in the range")

            #  a. If the guess greater than the solution, display to the player "It's lower".
            if (guess > answer):
                attempt += 1 
                print("It's Lower")
                
            #  b. If the guess is less than the solution, display to the player "It's higher".
            if (guess < answer):
                attempt += 1
                print("It's Higher")
                
        except ValueError:
                print("Please enter an integer")
        
        
    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    # and show how many attempts it took them to get the correct number.
    print("Got it! It took you {} guesses".format(attempt))
        
        # 5. Let the player know the game is ending, or something that indicates the game is over.
    print("Ending Game")
        
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()