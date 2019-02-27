count = [0, 0, 0, 0]

for i in range(3):
    a, b = map(int, input().split())
    count[a - 1] += 1
    count[b - 1] += 1

flag = True
for e in count:
    if e == 3:
        print("NO")
        flag = False
        break

if flag:
    print("YES")
