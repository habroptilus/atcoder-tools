N = int(input())
L = [2, 1]


def Lucas(n):
    """
    >>> Lucas(5)
    11
    >>> Lucas(86)
    939587134549734843
    """
    if len(L) > n:
        return L[n]
    else:
        L.append(Lucas(n - 1) + Lucas(n - 2))
        return L[n]


print(Lucas(N))
