N, Y = map(int, input().split())


def judge():
    for i in range(N + 1):
        for j in range(N + 1 - i):
            if i * 10000 + j * 5000 + (N - i - j) * 1000 == Y:
                return "{} {} {}".format(i, j, N - i - j)
    return "-1 -1 -1"


print(judge())
