from collections import Counter
c = Counter()
N = int(input())
for _ in range(N):
    a = int(input())
    c[a] += 1
count = 0
for key, value in c.items():
    if value % 2 != 0:
        count += 1
print(count)
