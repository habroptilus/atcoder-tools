N, M, X = map(int, input().split())

a = list(map(int, input().split()))
s = 0
assert len(a) == M
for i in range(M):
    if a[i] < X:
        s += 1
    else:
        break
print(min(len(a) - s, s))
