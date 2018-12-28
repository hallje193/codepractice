x = input('enter: ')
invx = x[::-1]

if invx == x:
    print('The phrase {} is a palindrome!'.format(x))
else:
    print('The phrase {} is not a palindrome...'.format(x))
