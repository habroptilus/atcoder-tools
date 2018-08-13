from collections import deque
N, M = map(int, input().split())
A = []
B = []
G = [[-1] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1
    A.append(a - 1)
    B.append(b - 1)


def BFS(G):  # 連結か判定する関数
    """
    >>> BFS([[-1, 1, 1], [1, -1, 1], [1, 1, -1]])
    True
    >>> BFS([[-1,1,-1], [1,-1,-1], [-1,-1,-1]])
    False
    >>> BFS([[-1,1,-1,-1], [1,-1,1,-1], [-1,1,-1,1], [-1,-1,1,-1]])
    True
    """
    q = deque()
    q.append(0)
    visited = [False] * len(G)
    while len(q) != 0:
        p = q.popleft()
        for j in range(len(G)):
            if G[p][j] == 1 and not visited[j]:
                q.append(j)
                visited[j] = True
    if False in visited:
        return False
    else:
        return True


count = 0
for i in range(M):
    G[A[i]][B[i]] = -1
    G[B[i]][A[i]] = -1
    if not BFS(G):
        count += 1
    G[A[i]][B[i]] = 1
    G[B[i]][A[i]] = 1
print(count)
