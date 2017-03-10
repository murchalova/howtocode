def listforsetti():
    l = [int(s) for s in input().split()]
    l2 = []
    s, s1 = 0, 0
    for i in range(len(l)):
        s += l[i]
    for k in range(1,len(l) - 1):
        s1 += l[k]
    l2.append(s)
    l2.append(max(l))
    l2.append(s1)
    return print(l2)

def del_dublicate():
    l = [int(s) for s in input().split()]
    for i in l:
        if l.count(i) != 1:
            l.remove(i)
    return print(l)

def together():
    li1 = [int(s) for s in input().split()]
    li2 = [int(s) for s in input().split()]
    li3 = li1 + li2
    return print(li3)

listforsetti()
del_dublicate()
together()