import math
N = int(input())
result = []
count = 0
i = 2


def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


while True:
    n = 5 * i + 1
    if isPrime(n):
        result.append(n)
        count += 1
    if count == N:
        break
    i += 1

print(" ".join(map(str, result)))
