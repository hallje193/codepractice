#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import time

#inputs
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

#Year the user will turn 100
yeartoday = int(time.strftime("%Y"))
year100 = yeartoday - age + 100

#Printing Statement
def PrintStatement():
    print('Hello {}! You will turn 100 on {}.'.format(name, year100), end="  ")
PrintStatement()
print('\n'*0)

#Print the number of loops
loopnum = int(input('Please enter a number: '))
for loopnum in range(0,loopnum):
    PrintStatement()
