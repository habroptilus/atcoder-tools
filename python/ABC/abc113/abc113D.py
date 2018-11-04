H, W, K = map(int, input().split())


def get_com(W):
    N = [i for i in range(W)]
    count = 0
    count_edge = 0

    for i in range(1 << len(N)):
        output = []
        flag = True
        for j in range(len(N)):
            if ((i >> j) & 1) == 1:
                if output[-1] + 1 == N[j]:
                    flag = False
                    break
                output.append(N[j])
        if flag:
            if output[0] == 0:
                count_edge += 1
            if output[0] == 1 or output[1] == 1:
                count += 1
    return count, count_edge


print(weight)
mod = 10**9 + 7
DP = [[None for j in range(W)] for i in range(H)]
DP[0][0] = 1
for i in range(1, W):
    DP[0][i] = 0

for h in range(1, H):
    for w in range(W):
        if w == 0:
            DP[h][w] = (DP[h - 1][w] + DP[h - 1][w + 1]) % mod
        elif w == W - 1:
            DP[h][w] = (DP[h - 1][w] + DP[h - 1][w - 1]) % mod
        else:
            DP[h][w] = (DP[h - 1][w] + DP[h - 1]
                        [w - 1] + DP[h - 1][w + 1]) % mod
print(DP[H - 1][K - 1])
