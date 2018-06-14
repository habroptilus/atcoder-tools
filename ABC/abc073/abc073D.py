from itertools import permutations
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
A = []
B = []
C = []
D = [[] for _ in range(N)]
inf = float("inf")
for i in range(N):
    for j in range(N):
        if i == j:
            D[i].append(0)
        else:
            D[i].append(inf)


for _ in range(M):
    a, b, c = map(int, input().split())
    D[a - 1][b - 1] = c
    D[b - 1][a - 1] = c


def WarshallFloyd(D):
    """
    >>> WarshallFloyd([[0, 1, 4], [1, 0, 1], [4, 1, 0]])
    [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    """
    for k in range(len(D)):
        for i in range(len(D)):
            for j in range(len(D)):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


D = WarshallFloyd(D)
Min = inf
for e in permutations(r):
    s = 0
    for i in range(R - 1):
        s += D[e[i] - 1][e[i + 1] - 1]
    Min = min(s, Min)

print(Min)
