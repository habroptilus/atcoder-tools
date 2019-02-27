L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]
for i in range(N):
    if L <= A[i] <= H:
        print(0)
    elif A[i] < L:
        print(L - A[i])
    else:
        print(-1)
