N, A, B = map(int, input().split())
mi = max(0, A + B - N)
ma = min(A, B)
print(ma, mi)
