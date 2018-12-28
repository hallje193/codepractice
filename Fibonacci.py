#Fibonacci Sequence
#Ask the user how many Fibonacci numbers to generate.

def main():
    print('Please enter the number of Fibonacci numbers to generate:')


    usernumber = input('')


    try:
        usernumber = int(usernumber)

    except:
        print('Invalid entry. Please try again')
        main()


    generate(usernumber)


    print('Would you like to generate again?  (y/n)')


    if input('') == 'y':
        main()

    else:
        quit()


def generate(usernumber):
    if usernumber == 1:
        fib_sequence = [1]

    else:
        fib_sequence = [1, 1]

        for i in range(2, usernumber):

            fib_number = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(fib_number)

    print(fib_sequence)


main()
