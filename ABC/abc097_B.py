X = int(input())

ans = 1
flag = False

for b in range(2, X):
    if flag:
        break
    p = 2
    while True:
        if b**p > X:
            if p != 2:
                ans = max(ans, b**(p - 1))
            else:
                flag = True
            break
        p += 1
print(ans)
