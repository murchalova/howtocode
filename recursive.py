def recursive(x):
    if x == 1:
        return print(1, end=' ')
    else:
        r = recursive(x-1)
        r = x
    return print(x, end=' ')

recursive(200)
