from cmath import pi

Num1 = input('Enter the first number:')
Num2 = input('Enter the second number:')

try:
 if float((Num1)) > float((Num2)):
     print(Num1,'is the biggest number', Num2, 'is the smollest number')
 else:
     print(Num2,'is the biggest number', Num1,'is the smollest number')
except ValueError:
  print(Num1+Num2+str(pi))








