H, W = map(int, input().split())
a = []
for i in range(H):
    a.append(list(map(int, input().split())))
count = 0
result = []
for i in range(H):
    j = 0
    while j < W:
        if a[i][j] % 2 != 0:
            s = j
            j += 1
            while j < W:
                if a[i][j] % 2 != 0 or j == W - 1:
                    a[i][s] -= 1
                    a[i][j] += 1
                    for k in range(s, j):
                        count += 1
                        result.append(((i, k), (i, k + 1)))
                    break
                j += 1
        j += 1

i = 0
while i < H:
    if a[i][-1] % 2 != 0:
        s = i
        i += 1
        while i < H:
            if a[i][-1] % 2 != 0 or i == H - 1:
                for k in range(s, i):
                    count += 1
                    result.append(((k, W - 1), (k + 1, W - 1)))
                break
            i += 1
    i += 1


print(count)
for e in result:
    print(e[0][0] + 1, e[0][1] + 1, e[1][0] + 1, e[1][1] + 1)
