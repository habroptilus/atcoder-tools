N = int(input())
a = [None]
for _ in range(N):
    a.append(int(input()))

x = 1
count = 0
while True:
    if x == 2:
        print(count)
        break
    if a[x] is None:
        print(-1)
        break
    else:
        count += 1
        temp = a[x]
        a[x] = None
        x = temp
