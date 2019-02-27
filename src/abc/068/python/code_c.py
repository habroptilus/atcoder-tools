from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# print(G)
INF = float("inf")


def BFS(G, s):
    n = len(G)
    q = deque()
    D = [INF] * n
    q.append(s)
    D[s] = 0
    while len(q) != 0:
        p = q.popleft()
        for i in G[p]:
            if D[i] == INF:
                q.append(i)
                D[i] = D[p] + 1
    if D[n - 1] == 2:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"


print(BFS(G, 0))
