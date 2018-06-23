N = int(input())
A = [0, 0, 0]
b = map(int, input().split())
for a in b:
    if a % 4 == 0:
        A[2] += 1
    elif a % 2 == 0:
        A[1] += 1
    else:
        A[0] += 1

# print(A)

for i in range(3):
    if A[i] != 0:
        s = i
        A[i] -= 1
        break


def judge(A, s, N):
    for i in range(N - 1):
        if s == 0:  # 割り切れない場合
            if A[2] != 0:
                A[2] -= 1
                s = 2
            else:
                return "No"
        elif s == 1:
            if A[1] != 0:
                A[1] -= 1
                s = 1
            elif A[2] != 0:
                A[2] -= 1
                s = 2
            else:
                return "No"
        else:
            if A[0] != 0:
                A[0] -= 1
                s = 0
            elif A[1] != 0:
                A[1] -= 1
                s = 1
            elif A[2] != 0:
                A[2] -= 1
                s = 2
            else:
                return "No"
    return "Yes"


print(judge(A, s, N))
