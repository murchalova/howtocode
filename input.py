from cmath import pi
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
n1 = input('Введите первое число:')
if isFloat(n1):
    n2 = input('Введите второе число:')
    if isFloat(n1) and isFloat(n2):
       if float(n1) > float(n2):
        print( n1, 'больше', n2)
       if float(n2) > float(n1):
        print(n2, 'больше', n1)
    else:
     print(n2 + str(pi))
else:
    print(n1 + str(pi))

if isFloat(n1) and isFloat(n2):
    res= float(n1)+float(n2)
    print('Их сумма', res)