H, W, K = map(int, input().split())


def get_com(W):
    N = [i for i in range(W)]
    weights = [0 for i in range(W)]

    for i in range(1 << len(N)):
        output = []
        flag = True
        for j in range(len(N)):
            if ((i >> j) & 1) == 1:
                if len(output) != 0 and output[-1] + 1 == N[j]:
                    flag = False
                    break
                output.append(N[j])
        if flag:
            for k in range(len(output)):
                weights[output[k]] += 1
    return weights


weight = get_com(3)
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
