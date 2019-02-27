N = int(input())
A = list(map(int, input().split()))


def solve(a):
    min_a = min([elem for elem in a if elem != 0])
    new_a = [elem % min_a for elem in a]
    if len([elem for elem in new_a if elem == 0]) == len(a):
        return min_a
    new_a[new_a.index(0)] = min_a
    return solve(new_a)


print(solve(A))
