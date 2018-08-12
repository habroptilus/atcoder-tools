N, M = map(int, input().split())
A = list(map(int, input().split()))
import collections

L = []
s = 0
for a in A:
    s += a
    L.append(s % M)
c = collections.Counter(L)

ans = 0
for k, v in c.items():
    if k == 0:
        ans += v * (v + 1) // 2
    else:
        ans += v * (v - 1) // 2

print(ans)
