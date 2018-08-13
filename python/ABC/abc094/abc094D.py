n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
a.remove(max_a)
min_diff = 1000000000
for a_i in a:
    if min_diff > abs(max_a / 2 - a_i):
        min_diff = abs(max_a / 2 - a_i)
        half_a = a_i
print(max_a, half_a)
