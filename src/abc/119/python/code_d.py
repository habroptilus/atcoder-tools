import bisect
A, B, Q = map(int, input().split())
INF = float("inf")
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]

for q in range(Q):
    x = int(input())
    ans = INF
    a_i = bisect.bisect_right(s, x)
    b_i = bisect.bisect_right(t, x)
    for a in [s[a_i], s[a_i - 1]]:
        for b in [t[b_i], t[b_i - 1]]:
            ans = min(ans, abs(x - a) + abs(b - a), abs(x - b) + abs(b - a))
    print(ans)
