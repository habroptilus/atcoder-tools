N = int(input())
words = []
prev = "hogehoge"


def check():
    for i in range(N):
        w = input()
        if (i != 0 and prev[-1] != w[0]) or (w in words):
            return "No"
        prev = w
        words.append(w)
    return "Yes"


print(check())
