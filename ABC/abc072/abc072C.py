from collections import Counter
N = int(input())
A = list(map(int, input().split()))
c = Counter()

for i in range(N):
    c[A[i]] += 1
    c[A[i] + 1] += 1
    c[A[i] - 1] += 1

print(max(c.values()))
