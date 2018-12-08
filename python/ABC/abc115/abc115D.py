N, X = map(int, input().split())


def solve(L, X):
    if L == 0 and X == 1:
        return 1
    if X == 1:
        return 0
    l = 2**(L + 1) - 3
    if 2 <= X <= l + 1:
        return solve(L - 1, X - 1)
    elif X == l + 2:
        return solve(L - 1, l) + 1
    elif l + 2 <= X <= 2 * l + 2:
        return solve(L - 1, l) + solve(L - 1, X - l - 2) + 1
    else:
        return 2 * solve(L - 1, l) + 1


print(solve(N, X))
