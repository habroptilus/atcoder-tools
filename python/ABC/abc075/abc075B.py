from itertools import product
H, W = map(int, input().split())
S = [["."] * (W + 2)]
for _ in range(H):
    s = ["."] + list(input()) + ["."]
    S.append(s)
S.append(["."] * (W + 2))

ans = []
deltas = list(product((0, 1, -1), (0, 1, -1)))
del deltas[0]


def count(S, i, j):
    if i <= 0 or i >= H + 1 or j <= 0 or j >= W + 1:
        return "error"
    c = 0
    for d_i, d_j in deltas:
        if S[i + d_i][j + d_j] == "#":
            c += 1
    return c


def print_grid(G):
    for i in range(len(G)):
        print("".join(G[i]))
    return


for i in range(1, H + 1):
    ans_row = []
    for j in range(1, W + 1):
        if S[i][j] == "#":
            ans_row.append("#")
        else:
            ans_row.append(str(count(S, i, j)))
    ans.append(ans_row)

# print_grid(S)
print_grid(ans)
