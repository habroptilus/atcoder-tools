"""
二分探索O(nlogn)でかいてみたらTLEして、通ってる回答みたら線形探索O(n**2)でもとおっててなんでという気持ち
二分探索で答えがもとまらず無限ループになってしまうケースがあるぽい？
"""
N = int(input())


def binary_search(L, target):
    """
    >>> binary_search([1,3,5],2)
    2
    >>> binary_search([1,3,5],5)
    0
    >>> binary_search([1,3,5],9)
    0
    >>> binary_search([1,3,3,3,3,5],3)
    1
    >>> binary_search([1,3,3,3,3,5],4)
    1
    """
    if L[0] > target:
        return len(L)
    if L[-1] <= target:
        return 0
    right_i = len(L) - 1
    left_i = 0
    while left_i + 1 != right_i:
        med_i = (right_i + left_i) // 2
        if L[med_i] < target:
            left_i = med_i
        elif L[med_i] > target:
            right_i = med_i
        else:
            while L[med_i + 1] == target:
                med_i += 1
            return len(L) - med_i - 1
    return len(L) - right_i


D = []
for _ in range(3):
    D.append(list(map(int, input().split())))
A, B, C = D
A.sort()
A = [-a for a in A]
A.sort()
C.sort()
ans = 0

for b in B:
    ans += binary_search(A, -b) * binary_search(C, b)

print(ans)
