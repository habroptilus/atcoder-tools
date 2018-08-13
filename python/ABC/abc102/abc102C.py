N = int(input())
A = list(map(int, input().split()))
A = [A[i - 1] - i for i in range(1, N + 1)]
A.sort()
if N % 2 == 1:
    b = A[(N - 1) // 2]
else:
    b = round((A[N // 2] + A[N // 2 - 1])) // 2
print(sum([abs(A[i] - b)for i in range(N)]))
