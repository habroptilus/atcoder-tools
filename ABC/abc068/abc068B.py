N = int(input())
max_count = 0
for i in range(2, N + 1):
    count = 0
    while i % 2 == 0:
        count += 1
        i //= 2
    max_count = max(max_count, count)

print(2**max_count)
