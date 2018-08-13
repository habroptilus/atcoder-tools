from itertools import product

N = int(input())
F = []
P = []
for _ in range(N):
    temp = list(map(int, input().split()))
    F.append([temp[:2], temp[2:4], temp[4:6], temp[6:8], temp[8:]])
for _ in range(N):
    P.append(list(map(int, input().split())))

prod = list(product((0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                    (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)))
MAX = -float("inf")


def compute(pattern):
    x = 0
    for i in range(N):
        c = 0
        for j in range(5):
            for k in range(2):
                if pattern[j][k] == 1 and F[i][j][k] == 1:
                    c += 1
        x += P[i][c]
    return x


del prod[0]
for e in prod:
    pattern = [e[:2], e[2:4], e[4:6], e[6:8], e[8:]]
    MAX = max(compute(pattern), MAX)

print(MAX)
