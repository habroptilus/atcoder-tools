N = int(input())


def max_square(n):
    """
    >>> max_square(10)
    9
    >>> max_square(81)
    81
    >>> max_square(271828182)
    271821169
    """
    base = 0
    while (base + 1)**2 <= n:
        base += 1
    return base**2


print(max_square(N))
