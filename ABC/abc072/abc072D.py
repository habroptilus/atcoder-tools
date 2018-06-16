N = int(input())
p = list(map(int, input().split()))
count = 0

for i in range(N):
    if p[i] == i + 1:
        if i == N - 1:
            temp = p[N - 2]
            p[N - 2] = p[N - 1]
            p[N - 1] = temp
            count += 1
        else:
            temp = p[i + 1]
            p[i + 1] = p[i]
            p[i] = temp
            count += 1

print(count)
