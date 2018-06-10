from collections import Counter, deque
import heapq


def Dijkstra(C):
    q = []
    inf = float("inf")
    f = [inf] * 11
    f[-1] = 0
    f[1] = 0
    heapq.heappush(q, (0, 1))
    while len(q) != 0:
        print(q)
        cost, index = heapq.heappop(q)
        if f[index] < cost:
            continue
        for i in range(10):
            if cost + C[index][i] < f[i]:
                f[i] = cost + C[index][i]
                heapq.heappush(q, (f[i], i))
    return f


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

f = Dijkstra(C)

print(f)
