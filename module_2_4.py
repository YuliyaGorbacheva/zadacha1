numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [0]
not_primes = [0]

for i in range(len(numbers)):
    for j in range(2, i):
        if (i % j) == 0:
            not_primes. append(i)
            break
        else:
            primes.append(i)
            break
print(primes)
print(not_primes)