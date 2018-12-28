A = ''
B = ''
C = ''
operator_index = 0

#Split up the input string into A, B and C variables
def SplitString(string):
    global A, B, C, operator_index

    if '*' in string:
        for i in range(0, string.index('*')):
            A += string[i]

        for i in range(string.index('*')+1, string.index('=')):
            B += string[i]

        operator_index = string.index('*')


    elif '/' in string:
        for i in range(0, string.index('/')):
            A += string[i]

        for i in range(string.index('/')+1, string.index('=')):
            B += string[i]

        operator_index = string.index('/')



    elif '+' in string:
        for i in range(0, string.index('+')):
            A += string[i]

        for i in range(string.index('+')+1, string.index('=')):
            B += string[i]

        operator_index = string.index('+')


    elif '-' in string:
        for i in range(0, string.index('-')):
            A += string[i]

        for i in range(string.index('-')+1, string.index('=')):
            B += string[i]

        operator_index = string.index('-')


    for i in range(string.index('=')+1, len(string)):
        C += string[i]



def getX(string):
    global A, B, C, operator_index
    SplitString(string)


    #If 'x' is on right side of equation
    if string.index('x') > string.index('='):
        if '*' in string:
            result = int(A) * int(B)

        elif '/' in string:
            result = int(A) / int(B)

        elif '+' in string:
            result = int(A) + int(B)

        elif '-' in string:
            result = int(A) - int(B)

        else:
            return 'Invalid String'


    #If 'x' is in 'A' position
    elif string.index('x') < operator_index:
        if '*' in string:
            result = int(C) / int(B)

        elif '/' in string:
            result = int(C) * int(B)

        elif '+' in string:
            result = int(C) - int(B)

        elif '-' in string:
            result = int(C) + int(B)

        else:
            return 'Invalid String'


    #If 'x' is in 'B' position
    elif string.index('x') > operator_index:
        if '*' in string:
            result = int(C) / int(A)

        elif '/' in string:
            result = int(A) / int(C)

        elif '+' in string:
            result = int(C) - int(A)

        elif '-' in string:
            result = int(A) - int(C)

        else:
            return 'Invalid String'

    else:
        return 'Invalid String'

    result = round(result, 2)

    return result



string = 'x*6=30'

print(getX(string))
