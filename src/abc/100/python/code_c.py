N = int(input())
A = list(map(int, input().split()))


def count(n):
    """
    >>> count(10)
    1
    >>> count(96)
    5
    """
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


s = 0
for i in range(N):
    s += count(A[i])

print(s)
