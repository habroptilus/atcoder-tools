from itertools import permutations
c = []
for i in range(3):
    c.append(list(map(int, input().split())))
S = sum([c[i][i] for i in range(3)])
perms = list(permutations([1, 2, 3], 3))


def judge(c, S):
    for p in perms:
        s = sum([c[i][p[i] - 1] for i in range(3)])
        if S != s:
            return "No"
    return "Yes"


print(judge(c, S))
