def divide(L):
    ans = []
    prev = 0
    for i in range(len(L)):
        if L[i] == 0:
            ans.append(L[prev:i])
            prev = i + 1
    ans.append(L[prev:])
    return ans


def extract(L, v):
    for i in range(len(L)):
        L[i] -= v
    return L


def ans(L):
    if L == [0] * len(L):
        return 0
    count = 0
    divided = divide(L)
    for l in divided:
        if len(l) == 0:
            continue
        m = min(l)
        count += m
        extracted = extract(l, m)
        count += ans(extracted)
    return count


N = int(input())
h = list(map(int, input().split()))
print(ans(h))
