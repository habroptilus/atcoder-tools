N, M = map(int, input().split())
A = map(int, input().split())
C = [2, 5, 5, 4, 5, 6, 3, 7, 6]
costs = {m: C[m - 1] for m in A}
dp = [0]
inf = float("inf")
for i in range(1, N + 1):
    dp.append(max([dp[i - c] if i - c >= 0 else -
                   inf for c in costs.values()]) + 1)
digits = list(costs.keys())

sorted(digits, reverse=True)

result = []
for i in range(dp[N]):
    for digit in digits:
        if dp[N - costs[digit]] == dp[N] - i - 1:
            result.append(str(digit))
            break

print("".join(result))
