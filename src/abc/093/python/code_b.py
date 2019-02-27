A, B, K = map(int, input().split())

if 2 * K > B - A:
    for i in range(B - A + 1):
        print(A + i)
else:
    for i in range(K):
        print(A + i)
    for j in range(B - K + 1, B + 1):
        print(j)
