from itertools import product
A, B, C, D = map(int, list(input()))
patterns = list(product(("+", "-"), ("+", "-"), ("+", "-")))
for pattern in patterns:
    temp = str(A) + pattern[0] + str(B) + \
        pattern[1] + str(C) + pattern[2] + str(D)
    if eval(temp) == 7:
        print(temp + "=7")
        break
