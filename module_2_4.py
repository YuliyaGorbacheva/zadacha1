numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_primes = True
    for j in range (2, i+1) :
        if i % j == 0 and i != j:
            is_primes = True
            not_primes. append(i)
            break
        elif i % j != 1 :
            is_primes = False
            primes. append(i)
            break

print(primes)
print(not_primes)