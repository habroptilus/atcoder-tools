from collections import Counter
from heapq import heappush, heappop
N, K = map(int, input().split())
sushi_list = []
for i in range(N):
    t, d = map(int, input().split())
    sushi_list.append((t, d))


sushi_list.sort(key=lambda x: x[1], reverse=True)
S_x = sushi_list[:K]
c = Counter()
f_p = 0

for t, d in S_x:
    c[t] += 1
    f_p += d

Q = []
R = []

for sushi in sushi_list:
    if sushi[0] in c.keys():
        if c[sushi[0]] > 1:
            heappush(Q, sushi[1])
    else:
        heappush(R, -sushi[1])
p = len(c)
ans = f_p + p**2

while True:
    print(Q, R)
    if len(Q) == 0 or len(R) == 0:
        break
    min_q = heappop(Q)
    max_r = -heappop(R)
    p += 1
    f_p = f_p + max_r - min_q
    ans = max(ans, f_p + p**2)

print(ans)
