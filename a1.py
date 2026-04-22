import random
number=random.randint(1, 100)

def intro():
    print('Can you tell me your name?')
    global Name
    name = input()
    print(name+ ',I hope you like games because I have an interesting one guess a number from 1_100')
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print('\nNumber is ', x)

    print('Go ahead.Guess!')

def pick():
        if guess<=100 and guess>=1:
                 if guess<number:
                         print('The guess you picked is small.')
                 if guess>number:
                         print('The guess you picked is too big.')

                         if guess>100 or guess<1:
                             print('inccorect guess')
intro()
guess=int(input('Enter you guess:'))
pick()
if guess == number:
    print('Good job! the guess you picked is great!!!!')


if guess != number:
    print('nope.the guess is incorrect.my number was ' + str(number))