N = int(input())
D, X = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

print(sum([int((D - 1) / A[i]) for i in range(N)]) + X + N)
