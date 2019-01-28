S = input()
T = input()


def check(A, B):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    d = {c: None for c in alphabets}
    for i in range(len(A)):
        if d[A[i]] is None:
            d[A[i]] = B[i]
        elif d[A[i]] != B[i]:
            return False
    return True


print("Yes" if check(S, T) and check(T, S) else "No")
