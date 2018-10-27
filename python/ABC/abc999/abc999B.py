A, B, K = map(int, input().split())
for i in range(K):
    if i % 2 == 0:
        if A % 2 != 0:
            A = A - 1
        A = A // 2
        B = B + A
    else:
        if B % 2 != 0:
            B = B - 1
        B = B // 2
        A = A + B
print(A, B)
