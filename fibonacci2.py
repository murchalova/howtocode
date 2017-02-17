listFib = []
def fib(i, f):
    m=1
    k=0
    while True:
        r = k + m
        m = k
        k = r
        if r > i:
            break
        listFib.append(r)
        listFib.join(map(str, f))
    return listFib
def print_fib(i, f):
    print(fib(i, f))
print_fib(200, 'ss')