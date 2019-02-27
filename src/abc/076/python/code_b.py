N = int(input())
K = int(input())

now_v = 1
for _ in range(N):
    if now_v < K:
        now_v *= 2
    else:
        now_v += K
print(now_v)
