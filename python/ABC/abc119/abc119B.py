N = int(input())
s = 0
for i in range(N):
    m, u = input().split()
    if u == "BTC":
        s += float(m) * 380000
    else:
        s += float(m)

print(s)
