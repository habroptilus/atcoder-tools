from collections import Counter, deque
import heapq


def Dijkstra(C, s):
    q = []
    inf = float("inf")
    f = [inf] * 11
    f[-1] = 0
    f[s] = 0
    heapq.heappush(q, (0, s))
    while len(q) != 0:
        # print(q)
        # print(f)
        cost, index = heapq.heappop(q)
        if index == 1:
            return f[index]
        if f[index] < cost:
            continue
        for i in range(10):
            if cost + C[index][i] < f[i]:
                f[i] = cost + C[index][i]
                heapq.heappush(q, (f[i], i))
    return "hoge"


H, W = map(int, input().split())
C = []
A = []
for _ in range(10):
    C.append(list(map(int, input().split())))

for _ in range(H):
    A.append(list(map(int, input().split())))

c = Counter()
for i in range(H):
    for j in range(W):
        c[A[i][j]] += 1
D = []
for i in range(10):
    D.append(Dijkstra(C, i))
D.append(0)
s = 0
for i, j in c.items():
    s += D[i] * j

print(s)
