#Palindrome with loops

#String entry
x = str(input('enter a string: '))

#Word reverse function
def reverse(x):
    invx = ''
    for i in range(len(x)):
        invx += x[len(x)-1-i]
    return invx

#Interrorgate entry word with reverse
invx = reverse(x)

if invx == x:
    print('The phrase {} is a palindrome!'.format(x))

else:
    print('The phrase {} is not a palindrome...'.format(x))
