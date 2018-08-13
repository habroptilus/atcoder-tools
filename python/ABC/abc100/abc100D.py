from itertools import product
N, M = map(int, input().split())
X = []
Y = []
Z = []
for _ in range(N):
    x, y, z = list(map(int, input().split()))
    X.append(x)
    Y.append(y)
    Z.append(z)


def compute(xyz, opr):
    """
    >>> compute((1,2,3),("+","-","+"))
    2
    """
    x, y, z = xyz
    return eval(opr[0] + str(x) + opr[1] + str(y) + opr[2] + str(z))


oprs = list(product(("+", "-"), ("+", "-"), ("+", "-")))

Max = -float("inf")

for opr in oprs:
    L = [compute(xyz, opr) for xyz in zip(X, Y, Z)]
    L.sort()
    L.reverse()
    Max = max(Max, sum(L[:M]))

print(Max)
