H, W = map(int, input().split())
s = [["."] * (W + 2)]
for _ in range(H):
    s.append(["."] + list(input()) + ["."])
s.append(["."] * (W + 2))


def judge(s):
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if s[i][j] == "#":
                if s[i + 1][j] == "."and s[i][j + 1] == "."and s[i - 1][j] == "."and s[i][j - 1] == ".":
                    return "No"
    return "Yes"


print(judge(s))
