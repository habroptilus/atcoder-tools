s = int(input())
i = 1
l = [1, 2, 4]
while True:
    if s in l:
        print(i + 3)
        break
    i += 1
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
