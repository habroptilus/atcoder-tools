from collections import deque
H, W = map(int, input().split())
inf = float("inf")
s = [["#"] * (W + 2)]
D = [[inf] * (W + 2)]
white_num = 0
for i in range(H):
    main = list(input())
    white_num += len([e for e in main if e == "."])
    s.append(["#"] + main + ["#"])
    D.append([inf] * (W + 2))
s.append(["#"] * (W + 2))
D.append([inf] * (W + 2))


def BFS():  # 幅優先探索
    global D
    D[1][1] = 1
    q = deque()
    q.append((1, 1))
    while len(q) != 0:
        p = q.popleft()
        for e in [(p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0], p[1] - 1)]:
            if s[e[0]][e[1]] == "." and D[e[0]][e[1]] == inf:
                D[e[0]][e[1]] = D[p[0]][p[1]] + 1
                q.append(e)
                if e == (H, W):
                    return white_num - D[H][W]
    return -1


print(BFS())
