from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    l, r, d = map(int, input().split())
    G[l - 1].append((r - 1, d))
    G[r - 1].append((l - 1, -d))
q = deque()

x = [None] * N


def _BFS(start):
    q.append(start)
    while len(q) != 0:
        p = q.popleft()
        for index, d in G[p]:
            if x[index] is None:
                x[index] = x[p] + d
                q.append(index)
            elif x[index] != x[p] + d:
                return False
    return True


def BFS():
    for i in range(N):
        if x[i] is None:
            x[i] = 0
            if not _BFS(i):
                return "No"
    return "Yes"


print(BFS())
