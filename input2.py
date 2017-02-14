from cmath import pi

Num1 = input('Enter the first number:')
Num2 = input('Enter the second number:')

if Num1.isdigit() and Num2.isdigit():
    if int(Num1) > int(Num2):
        print(Num1,Num2)
    else: print(Num2,Num1)
else: print(Num1+Num2+str(pi))









