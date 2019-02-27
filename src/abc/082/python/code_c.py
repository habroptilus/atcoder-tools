from collections import Counter

N = int(input())
A = list(map(int, input().split()))

mycounter = Counter(A)
count = 0
for item in mycounter.items():
    if item[0] < item[1]:
        count += item[1] - item[0]
    elif item[1] < item[0]:
        count += item[1]

print(count)
