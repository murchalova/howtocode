import numc

def Name():
    n = input('Enter your name: ')
    return n

def evenOdd(x):
    if x % 2 == 0:
        x = 'even number.'
    else:
        x = 'odd number.'
    return x

def printALL():
    n = Name()
    c = numc.Number(n)
    i = evenOdd(c)
    print('Hello, ' + n + '!','You have '+ str(c) +' characters in your name.', 'It is an ' + str(i), sep='\n')

printALL()
