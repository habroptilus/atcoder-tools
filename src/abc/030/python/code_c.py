N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
hour = 0
a_i = 0
b_i = 0
finished = False
while True:
    while True:
        if a_i == N:
            finished = True
            break
        if a[a_i] < hour:
            a_i += 1
        else:
            break

    if finished:
        break
    hour = X + a[a_i]

    while True:
        if b_i == M:
            finished = True
            break
        if b[b_i] < hour:
            b_i += 1
        else:
            break

    if finished:
        break
    hour = Y + b[b_i]
    count += 1

print(count)
