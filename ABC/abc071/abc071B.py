from collections import Counter
S = list(input())
A = list("abcdefghijklmenopqrstuvwxyz")


def ans(S):
    for a in A:
        if a not in S:
            return a
    return "None"


print(ans(S))
