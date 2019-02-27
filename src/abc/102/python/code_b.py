N = int(input())
A = list(map(int, input().split()))
m = -float("inf")
for i in range(N):
    for j in range(N):
        m = max(abs(A[i] - A[j]), m)
print(m)
