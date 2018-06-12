N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()


def hoge():
    count = 0
    Ai = -1
    Ci = -1
    for i in range(N):
        if Ai < N - 1:
            while A[Ai + 1] < B[i]:
                Ai += 1
                if Ai == N - 1:
                    break
        if Ci < N - 1:
            while C[Ci + 1] <= B[i]:
                Ci += 1
                if Ci == N - 1:
                    break
        count += (Ai + 1) * (N - (Ci + 1))
    return count


print(hoge())
