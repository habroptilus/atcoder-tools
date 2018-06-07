from collections import Counter
N, K = map(int, input().split())
A = map(int, input().split())

c = Counter()

for a in A:
    c[a] += 1
values = []
for v in dict(c).values():
    values.append(v)
values.sort()
print(sum(values[:len(values) - K]))
