from functools import reduce
N = int(input())
T = []
for _ in range(N):
    T.append(int(input()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    if b > a:
        b, a = a, b
    return a * b // gcd(a, b)


x = reduce(lcm, T)
print(x)
