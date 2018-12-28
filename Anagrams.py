#Program to find how many strings in a array are anagrams with given string
import random

#Generate array with inputs of array size and length
def generate_array(array_size, array_length):
    array = []
    chars = 'abcdefghijklmnopqrstuvwqxyz'

    for i in range(0, array_size):
        array_entry = ''

        for j in range(0, array_length):
            array_entry += chars[random.randint(0,26)]

        array.append(array_entry)

    return(array)


#Main Body
def main():
    print('Please enter desired array size:')
    array_size = int(input(''))

    print('\nPlease enter desired array length:')
    array_length = int(input(''))

    print('\nPlease enter a string:')
    input_string = input('')

    array = generate_array(array_size, array_length)

    check_array(array, input_string, array_size, array_length)



#Checking array for anagrams
def check_array(array, input_string, array_size, array_length):
    num_anagrams = 0

    for i in range(0, array_size):
        copy_string = list(input_string)
        array_string = list(array[i])

        for j in range(0, len(input_string)):
            if input_string[j] in array_string:
                array_string.remove(input_string[j])
                copy_string.remove(input_string[j])

        if copy_string == []:
            num_anagrams += 1

    print('Array is:\n', array)
    print('Number of anagrams:  ', num_anagrams)

main()
