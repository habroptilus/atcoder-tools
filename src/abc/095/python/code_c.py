A, B, C, X, Y = map(int, input().split())
result = 0
m = min(X, Y)
if A + B < 2 * C:
    result += m * (A + B)
    if m == X:
        result += (Y - m) * B
    else:
        result += (X - m) * A
else:

    if m == X:
        if B > 2 * C:
            result += 2 * max(X, Y) * C
        else:
            result += 2 * m * C + (Y - m) * B
    else:
        if A > 2 * C:
            result += 2 * max(X, Y) * C
        else:
            result += 2 * m * C + (X - m) * A

print(result)
