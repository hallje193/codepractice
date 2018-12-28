#Request user input and check if it is a prime number.

def invalid_entry():
    try_again = ''
    try_again = input('Invalid entry. Would you like to try again?   (y/n)   ')

    if try_again == 'y':
        main()

    else:
        quit()


def request_input():
    try:
        return(int(input('Please enter a number:   ')))

    except:
        invalid_entry()


def calculate(user_input):
    divisors = []

    for i in range(1, user_input+1):
        if user_input % i == 0:
            divisors.append(i)

    if divisors == [1, user_input]:
        return '{} is a prime number!'.format(user_input)

    else:
        return '{} is not a prime number...'.format(user_input)


def main():
    run = True

    while run == True:
        user_input = request_input()

        result = calculate(user_input)

        print(result)

        if input('Would you like to continue?  (y/n)   ') != 'y':
            quit()



main()
