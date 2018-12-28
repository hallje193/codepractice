#Rock Paper Scissors Game
import random

wins = 0
losses = 0
ties = 0

def convert_to_integer(string):
    if string == 'rock':
        return 1
    elif string == 'paper':
        return 2
    elif string == 'scissors':
        return 3


def convert_to_text(integer):
    if integer == 1:
        return 'rock'
    elif integer == 2:
        return 'paper'
    elif integer == 3:
        return ' scissors'


def letsplay(player_input):
    global wins, losses, ties

    computer_input = random.randint(1,3)
    print('Computer has chosen: {}\n'.format(convert_to_text(computer_input)))

    if player_input - computer_input == 1 or player_input - computer_input == -2:
        print('You have won!')
        wins += 1

    elif player_input - computer_input == 0:
        print("It's a tie...")
        ties += 1

    else:
        print('You lost :(')
        losses += 1


def __main__():
    global wins, losses, ties

    play = True
    while play == True:
        player_input = input("\n\nPlease enter your play:   ")

        if player_input == "quit":
            rounds = wins + losses + ties

            if rounds == 0:
                print('\n\nThanks for playing!\n'
                "Sorry you didn't play this time.\n"
                'Please play again next time!\n\n\n')

            else:
                print('\n\nThanks for playing!\n'
                'Your stats for this game were:\n\n'
                'Wins: {} - {}%\n'
                'Losses: {} - {}%\n'
                'Number of Rounds: {}\n\n\n'.format(wins, round(wins/rounds*100,2), losses,
                round(losses/rounds*100,2), rounds))

            return False

        if player_input not in ['rock', 'paper', 'scissors', 'quit']:
            print('Invalid entry - please try again!')

        else:
            player_input = convert_to_integer(player_input)
            letsplay(player_input)



#Start the game!
print("\n\n\n\n\n::::::::::::::::::::::::::::::\n"
"Welcome to Rock-Paper-Scissors!\n\n"
"In this game, you will play against me - your computer.\n"
"You may choose from the following choices: \n \n"
"rock \n"
"paper \n"
"scissors\n\n"
"If at any time you would like to quit, just type 'quit'."
"\nLet's play!\n"
"::::::::::::::::::::::::::::::\n\n\n")

__main__()
