N, K = map(int, input().split())
s = []
for i in range(N):
    s.append(int(input()))

temp = []
prod = 1
ans = 0
flag = True
for i in range(N):
    if s[i] == 0:
        print(N)
        flag = False
        break
    if prod * s[i] <= K:
        temp.append(s[i])
        prod *= s[i]
    elif len(temp) == 0:
        continue
    elif prod // temp[0] * s[i] <= K:
        prod //= temp[0]
        prod *= s[i]
        del temp[0]
        temp.append(s[i])
    else:
        ans = max(len(temp), ans)
        prod = 1
        temp = []

if flag:
    print(max(len(temp), ans))
