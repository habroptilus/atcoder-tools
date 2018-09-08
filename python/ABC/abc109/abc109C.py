def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


N, X = map(int, input().split())

x = list(map(int, input().split()))

dist_list = [abs(X - e) for e in x]

ans = dist_list[0]
for e in dist_list:
    ans = gcd(ans, e)


print(ans)
