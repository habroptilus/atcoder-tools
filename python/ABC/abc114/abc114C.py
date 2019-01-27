import itertools
N = int(input())
p = 3
digits = [3, 5, 7]
A = []
flag = False
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
count = 0
for a in A:
    if "3" in str(a) and "5" in str(a) and "7" in str(a):
        count += 1
print(count)
