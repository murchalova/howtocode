listFib = []
def fib(i):
    m=1
    k=0
    while True:
        r = k + m
        m = k
        k = r
        if r > i:
            break
        listFib.append(r)
    return listFib
def print_fib(i):
    print(fib(i))
print_fib(200)