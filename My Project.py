from random import randrange
import time

name = input('Hello... Please enter your name: ')
print('Hello ' + name + '...Enter the number of times you want to spin the die')

def Die(num):                                                                                               #defines the function Die
    for i in range(0, int(num)):
     time.sleep(1)
     value = randrange(1,6)
     print('+-------------+')
     if value == 1:
        print('   |       |   ')
        print('   |   *   |   ')
        print('   |       |   ')
     elif value == 2:
        print('   |*      |   ')
        print('   |       |   ')
        print('   |      *|   ')
     elif value == 3:
        print('   |*      |   ')
        print('   |   *   |   ')
        print('   |      *|   ')
     elif value == 4:
        print('   |*     *|   ')
        print('   |       |   ')
        print('   |*     *|   ')
     elif value == 5:
        print('   |*     *|   ')
        print('   |   *   |   ')
        print('   |*     *|   ')
     elif value == 6:
        print('   |*  *  *|   ')
        print('   |       |   ')
        print('   |*  *  *|   ')
     else:
        print(" *** Error: illegal die value ***")
        print("+-------+")
roll = Die(input())

while True:
    print('Do you wanna roll again[Y/N]??')
    ask = input()
    if ask == 'Y' or 'y' in ask:
        name = input("Oh.. Let's continue... Please enter your name: ")
        print('Hello ' + name + '...Enter the number of times you want to spin the die')
        roll = Die(input())
    elif ask == 'N' or 'n':
            print('Oh.. Ok.. Byee')
            break