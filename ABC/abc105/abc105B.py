N = int(input())


def judge(N):
    i = 0
    while True:
        if 4 * i > N:
            break
        j = 0
        while True:
            if 4 * i + 7 * j == N:
                return "Yes"
            elif 4 * i + 7 * j > N:
                break
            else:
                j += 1
        i += 1
    return "No"


print(judge(N))
