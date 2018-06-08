N = int(input())
A = map(int, input().split())
counter = []
for a in A:
    count = 0
    while True:
        if a % 2 != 0:
            counter.append(count)
            break
        count += 1
        a = int(a / 2)

print(min(counter))
