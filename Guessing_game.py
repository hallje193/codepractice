#Guessing Game:
#User inputs a number between 1 and 9 until it matches the random value.
import random


#Evaluate the user input
def evaluate(input, randomvalue):
    if input == 'q':
        quit()

    try:
        input = int(input)

    except:
        print('Invalid entry!', end=' ')
        return True

    if input not in range(1,10):
        print('Invalid entry!', end=' ')
        return True

    elif input > randomvalue:
        print('Too high!\n')
        return True

    elif input < randomvalue:
        print('Too low!\n')
        return True

    elif input == randomvalue:
        print('Congratulations! You got it!\n')
        return False


def main():
    print('\n\n\n\nWelcome to the Guessing Game!\n\n\n'
    "Let's play a game\n"
    'Here are the rules:   You will enter a single digit number to try and guess my number.\n'
    '\nReady?\n')

    startgame()


def startgame():
    randomvalue = random.randint(1,9)
    playing = True
    userinput = ''

    while playing == True:
        userinput = input('\nPlease enter a number between 1 and 9:    ')
        playing = evaluate(userinput, randomvalue)

    if input('Would you like to play again?  (y/n)      ') == 'y':
        startgame()


main()
