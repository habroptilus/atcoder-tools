from functools import reduce
from itertools import combinations
N = int(input())
S = {"M": [], "A": [], "R": [], "C": [], "H": []}
for _ in range(N):
    i = input()
    head = i[0]
    if head == "M":
        S["M"].append(i)
    elif head == "A":
        S["A"].append(i)
    elif head == "R":
        S["R"].append(i)
    elif head == "C":
        S["C"].append(i)
    elif head == "H":
        S["H"].append(i)
counter = [len(S[head]) for head in list("MARCH") if len(S[head]) != 0]
combs = list(combinations(counter, 3))
ans = sum([reduce(lambda x, y: x * y, e) for e in combs])
print(ans)
