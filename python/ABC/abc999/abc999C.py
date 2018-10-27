
N = int(input())
A = []


def solve(k, A):
    if abs(A[k] - A[0]) > abs(A[k] - A[-1]):
        b = abs(A[k] - A[0])
        del A[k]
        return _solve(True, A) + b
    elif abs(A[k] - A[0]) < abs(A[k] - A[-1]):
        b = abs(A[k] - A[-1])
        del A[k]
        return _solve(False, A) + b
    else:
        b_top = abs(A[k] - A[0])
        b_tail = abs(A[k] - A[-1])
        del A[k]
        temp = A[:]
        return max(_solve(True, temp) + b_top, _solve(False, A) + b_tail)
    return ans


def _solve(from_top, A):
    ans = 0
    pos = {"top": 0, "tail": N - 2}
    if from_top:
        next = "top"
    else:
        next = "tail"

    while True:
        ans += abs(A[pos["top"]] - A[pos["tail"]])
        if next == "top":
            if pos["top"] + 1 == pos["tail"]:
                return ans
            else:
                pos["top"] += 1
                next = "tail"
        else:
            if pos["top"] == pos["tail"] - 1:
                return ans
            else:
                pos["tail"] -= 1
                next = "top"


for i in range(N):
    a = int(input())
    A.append(a)

A.sort()
ans = 0
for i in range(N):
    temp = A[:]
    hoge = solve(i, temp)
    ans = max(hoge, ans)


print(ans)
