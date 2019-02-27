N, K = map(int, input().split())
sushi_list = []
max_d = [0] * N
for i in range(N):
    t, d = map(int, input().split())
    sushi_list.append((t - 1, d))
    max_d[t - 1] = max(max_d[t - 1], d)

sushi_list.sort(key=lambda x: x[1], reverse=True)
good = []
for i in range(N):
    if max_d[sushi_list[i][0]] == sushi_list[i][1]:
        good.append(True)
        max_d[sushi_list[i][0]] = 0
    else:
        good.append(False)

s = sum([sushi[1] for sushi in sushi_list[:K]])
p = len(set([sushi[0] for sushi in sushi_list[:K]]))
ans = s + p**2
r = K - 1
l = K
while True:
    while r >= 0 and good[r]:
        r -= 1
    while l < N and not good[l]:
        l += 1
    if r < 0 or l >= N:
        break
    s = s - sushi_list[r][1] + sushi_list[l][1]
    p += 1
    ans = max(ans, s + p**2)
    r -= 1
    l += 1

print(ans)
