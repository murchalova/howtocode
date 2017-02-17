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

def print_fib(i,a):
     print(a.join(str(i) for i in fib(i)))

print_fib(20, ' | ')