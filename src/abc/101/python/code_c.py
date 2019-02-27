N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] == 1:
        x = i
        break

y = N - x - 1
ans = float("inf")


def ceil(m, n):
    return -(-m // n)


for s in range(K):
    t = K - 1 - s
    ans = min(ans, ceil(y - t, K - 1) + ceil(x - s, K - 1))

print(ans + 1)
