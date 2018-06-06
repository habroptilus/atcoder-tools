N = int(input())
C = []
S = []
F = []
for i in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)


def departure_t(t, j):
    if t < S[j]:
        return S[j]
    elif t % F[j] == 0:
        return t
    else:
        return t - t % F[j] + F[j]


for i in range(N):
    t = 0
    for j in range(i, N - 1):
        t = departure_t(t, j)
        t += C[j]
    print(t)
