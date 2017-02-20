def Recursive(x):
    if x == 1:
        return print(1, end=' ')
    else:
        r = Recursive(x-1)
        r = x
    return print(x, end=' ')

Recursive(200)
