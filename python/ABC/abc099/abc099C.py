N = int(input())


def count(base, total):
    count = 0
    exp = 1
    while exp * base <= total:
        exp *= base
    remain = total
    while exp != 1:
        count += remain // exp
        remain %= exp
        exp //= base
    count += remain
    return count


Min = float("inf")
for i in range(N + 1):
    c = 0
    c += count(6, i)
    c += count(9, N - i)
    Min = min(Min, c)
print(Min)
