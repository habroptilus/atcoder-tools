N, M = map(int, input().split())
cakes = []
for _ in range(N):
    cake = list(map(int, input().split()))
    cakes.append(cake)


def evaluation(pattern):
    """
    >>> evaluation([1,2,-3])
    6
    >>> evaluation([1,-20,-3])
    24
    """

    return sum([abs(pattern[i]) for i in range(3)])


DP = [[None] * (M + 1) for _ in range(N + 1)]
for i in range(N + 1):
    DP[i][0] = [0, 0, 0]

for i in range(N):
    for k in range(1, min(M + 1, i + 2)):
        new = []
        for j in range(3):
            new.append(DP[i][k - 1][j] + cakes[i][j])
        #print(i + 1, k)
        if k == i + 1:
            DP[i + 1][k] = new
            break
        if evaluation(DP[i][k]) > evaluation(new):
            DP[i + 1][k] = DP[i][k]
        else:
            DP[i + 1][k] = new

# print(DP[N][M])
print(evaluation(DP[N][M]))
