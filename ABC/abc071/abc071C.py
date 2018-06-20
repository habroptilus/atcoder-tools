from collections import Counter
N = int(input())
A = list(map(int, input().split()))
top1 = 0
top2 = 0
c = Counter()

for a in A:
    c[a] += 1
    if c[a] % 2 == 0:
        L = [a, top1, top2]
        L.sort()
        top1 = L[2]
        top2 = L[1]
print(top1 * top2)
