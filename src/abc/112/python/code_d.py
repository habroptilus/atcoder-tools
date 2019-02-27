import numpy as np
N, M = map(int, input().split())
ans = 0
for i in range(1, int(np.sqrt(M)) + 2):
    if M % i == 0:
        if min(M // i, i) >= N:
            ans = max(ans, max(M // i, i))
        elif max(M // i, i) >= N:
            ans = max(ans, min(M // i, i))

print(ans)
