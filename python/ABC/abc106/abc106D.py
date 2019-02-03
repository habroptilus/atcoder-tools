N, M, Q = map(int, input().split())
A = [[0] * N for _ in range(N)]
for _ in range(M):
    l, m = map(int, input().split())
    A[l - 1][m - 1] += 1

questions = []
for _ in range(Q):
    p, q = map(int, input().split())
    questions.append((p - 1, q - 1))


D = []
for l in range(N):
    s = 0
    d = []
    for r in range(N):
        s += A[l][r]
        d.append(s)
    D.append(d)

T = []
for r in range(N):
    s = 0
    t = []
    for l in range(N):
        s += D[N - l - 1][r]
        t.append(s)
    T.append(list(reversed(t)))

for question in questions:
    print(T[question[1]][question[0]])
