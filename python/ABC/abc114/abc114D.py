from collections import Counter
N = int(input())
c = Counter()
for n in range(2, N + 1):
    i = 2
    while i**2 <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count != 0:
            c[i] += count
        i += 1
    if n > 1:
        c[n] += 1

d = Counter()
for v in c.values():
    if 2 <= v:
        d["3"] += 1
    if 4 <= v:
        d["5"] += 1
    if 14 <= v:
        d["15"] += 1
    if 24 <= v:
        d["25"] += 1
    if 74 <= v:
        d["75"] += 1

ans = 0
ans += d["75"]
ans += (d["5"] - 1) * d["15"]
ans += (d["3"] - 1) * d["25"]
ans += (d["3"] - 2) * d["5"] * (d["5"] - 1) // 2
print(ans)
