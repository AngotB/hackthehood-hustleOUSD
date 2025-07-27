# Guessing Game - Angel, Antonio, Nelson

import random

#This function generates a random number and returns it to use in the game
def generate_random_number():
    random_number = random.randint(1, 100)
    return int(random_number)

#This function takes an user's guess between 1 and 100 and checks if the guess is within that range, if so, it returns the value, if its not, it errors out
def get_user_guess():
    guess = False
    #The loop will iterate until a valid guess within range is given
    while guess == False:
        print()
        print('guess the number between 1 and 100')
        print()
        user_guess = int(input())
        #If the user's guess is within range the function will return the guess to use it in the game
        if 1 <= user_guess <= 100:
            guess = True
            return user_guess
        #else the code will display an error message prompting the user to display a number within range.
        else:
            print()
            print('Your guess is out of range, please enter a number between 1 and 100')
            print()

#This function combines the past two functions in order to make the game work. It generates a random number and the takes the user's guess, if the guess is right it display the win text.
#If not, it tells the user if their guess was too high or too low. this function counts how many attempts were made until the right answer was achieved
def play_guessing_game():
    secret_number = generate_random_number()
    guess_correct = False
    attempts = 0
    #while the user has not guessed the number correctly the code will keep prompting th user for number input whie counting th attepts that have been done until the right number is guessed
    while guess_correct == False:
        users_guess = int(get_user_guess())
        #If the user guesses the number correctly the game will display congratulation message with attempts count and the right number on the terminal
        if users_guess == secret_number:
            guess_correct = True
            attempts += 1
            print()
            print(f'you are correct! The right number was {secret_number} you guessed the number in {attempts} attempts!')
            print()
        #Else if the users guess is below the right number, the code will alert the user of this in the terminal
        elif users_guess < secret_number:
            print()
            print('WRONG! number is too low!')
            print()
            attempts += 1
        #else the code will tell the user their guess is too high
        else:
            print()
            print('WRONG! number is too high!')
            print()
            attempts += 1 

#This function is the interface that allows the user to decide if they want to play or not and if they want to play AGAIN or not after they win a game
def game_loop():
    playing = False
    print()
    print('do you wish to play the number guessing game?')
    print()
    answer = input()
    #if user accepts playing the game the code proceeds to next step
    if answer == 'yes':
        playing = True
        #while the user is playing if they win the code proceeds, else the user must keep playing
        while playing == True:
            winner = False
            play_guessing_game()
            winner = True
            #If the user wins the game congratulates the user and asks them if they want to keep playing. if so then the game starts over, else the code finishes
            if winner == True:
                print()
                print('thank you for playing!')
                print('Do you wish to play again?')
                print()
                choice = input()
                if choice == 'yes':
                    continue
                elif choice == 'no':
                    print()
                    print('Goodbye!')
                    print()
                    break
    
    # if user DOES NOT accept playing the game the code exits
    elif answer == 'no':
        print()
        print('ok, bye!')
        print()

if __name__ == "__main__": 
    game_loop()





        
   
 

    





