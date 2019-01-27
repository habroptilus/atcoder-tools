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


def num(m):  # 指数がm-1以上の素因数の個数を求める
    return len(list(filter(lambda x: x >= m - 1, c.values())))


ans = 0
ans += num(75)
ans += (num(5) - 1) * num(15)
ans += (num(3) - 1) * num(25)
ans += (num(3) - 2) * num(5) * (num(5) - 1) // 2
print(ans)
