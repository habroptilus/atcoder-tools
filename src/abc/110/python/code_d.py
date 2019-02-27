N, M = map(int, input().split())


def combination(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(n - r + 1, n + 1):
        result *= i
    for i in range(1, r + 1):
        result //= i
    return result


def factorize(x):
    i = 2
    result = {}
    while True:
        if i**2 > x:
            break
        count = 0
        while x % i == 0:
            x //= i
            count += 1
        if count != 0:
            result[i] = count
        i += 1
    if x > 1:
        result[x] = 1
    return result


ans = 1
mod = 10**9 + 7
result = factorize(M)
for e in result.values():
    comb = combination(e + N - 1, e) % mod
    ans = ans * comb % mod

print(ans)
