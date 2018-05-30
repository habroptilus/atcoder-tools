from functools import reduce
from itertools import combinations
N = int(input())
S = {"M": set([]), "A": set([]), "R": set([]), "C": set([]), "H": set([])}
for _ in range(N):
    i = input()
    head = i[0]
    if head == "M":
        S["M"].add(i)
    elif head == "A":
        S["A"].add(i)
    elif head == "R":
        S["R"].add(i)
    elif head == "C":
        S["C"].add(i)
    elif head == "H":
        S["H"].add(i)
result = [len(S[head]) for head in list("MARCH") if len(S[head]) != 0]

ans = sum([reduce(lambda x, y: x * y, list(combinations(result, 3))[i])
           for i in range(len(result))])
print(ans)
