N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
sa = [X[i + 1] - X[i] for i in range(M - 1)]
sa.sort()
if N >= M:
    print(0)
else:
    print(sum(sa[:M - N]))
