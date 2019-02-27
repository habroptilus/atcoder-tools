N, M = map(int, input().split())
B = []
for i in range(M):
    (a, b) = map(int, input().split())
    B.append((a, b))
B = sorted(B, key=lambda x: x[0])


def update(x, y):
    if x[0] == y[0]:
        return (x[0], min(x[1], y[1]))
    if x[1] <= y[0]:
        return False
    else:
        return (y[0], min(x[1], y[1]))


now = B[0]
count = 0
for i in range(1, M):
    ans = update(now, B[i])
    # print(ans)
    if ans:
        now = ans
    else:
        count += 1
        now = B[i]
count += 1
print(count)
