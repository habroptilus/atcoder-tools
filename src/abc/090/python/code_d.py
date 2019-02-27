N, K = map(int, input().split())


def count_a(b, N, K):
    p = int((N + 1) / b)
    r = (N + 1) % b
    return (b - K) * p + max(0, r - K)


count = 0

for b in range(K + 1, N + 1):
    count += count_a(b, N, K)
    if K == 0:
        count -= 1
print(count)
