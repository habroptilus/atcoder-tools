K = int(input())
sunuke = list(range(1, 10))


def value(n):
    S = sum(map(int, list(str(n))))
    return n / S


def conmbine(left, nine_digits):
    return int(str(left) + str(9) * nine_digits)


if K <= 9:
    for i in range(K):
        print(sunuke[i])
else:
    prev = 1
    nine_digits = 1
    left = 1
    k = 9
    x = conmbine(left, nine_digits)
    v = value(x)
    while True:
        if prev <= v:
            sunuke.append(x)
            prev = v
            k += 1
            left += 1
            x = conmbine(left, nine_digits)
            v = value(x)
            if k == K:
                break
        else:
            nine_digits += 1
            left = 1
            x = conmbine(left, nine_digits)
            v = value(x)
    for i in range(K):
        print(sunuke[i])
