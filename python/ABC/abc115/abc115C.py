N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
ans = 10**12
for i in range(N - K + 1):
    ans = min(ans, h[i + K - 1] - h[i])

print(ans)
