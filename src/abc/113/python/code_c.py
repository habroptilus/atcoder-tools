N, M = map(int, input().split())
X = [[] for _ in range(N)]
ans_list = ["a" for i in range(M)]
for i in range(M):
    p, y = map(int, input().split())
    X[p - 1].append((i, y))
for i in range(N):
    if len(X[i]) != 0:
        X[i].sort(key=lambda x: x[1])
        for j in range(len(X[i])):
            ans_list[X[i][j][0]] = "{:06}".format(
                i + 1) + "{:06}".format(j + 1)

for i in range(len(ans_list)):
    print(ans_list[i])
