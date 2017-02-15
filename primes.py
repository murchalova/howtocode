primes = list(range(200))

i = 2
while i < 200:
    if primes[i] != 0:
        j = i * 2
        while j < 200:
            primes[j] = 0
            p = j + i
            j = p
    i = i + 1

for s in primes:
    if primes[s] != 0:
        print(primes[s], end=' ')

