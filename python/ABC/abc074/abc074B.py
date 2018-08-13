N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    if x < K / 2:
        ans += 2 * x
    else:
        ans += 2 * (K - x)
print(ans)
