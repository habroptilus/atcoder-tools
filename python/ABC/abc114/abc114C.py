import itertools
N = int(input())
digits = [3, 5, 7]


def get_A_product(digits, N):
    A = []
    flag = False
    p = 3
    while True:
        for tup in itertools.product(digits, repeat=p):
            a = int("".join(list(map(str, tup))))
            if a > N:
                flag = True
                break
            A.append(a)
        if flag:
            break
        p += 1
    return A


count = 0
A = get_A_product(digits, N)
for a in A:
    if all(str(a).count(c) > 0 for c in '753'):
        count += 1
print(count)
