N = int(input())
a = list(map(int, input().split()))
s = sum(a)
t = 0
Min = float("inf")
for i in range(N - 1):
    t += a[i]
    s -= a[i]
    Min = min(Min, abs(s - t))

print(Min)
