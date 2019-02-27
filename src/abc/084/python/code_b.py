A, B = map(int, input().split())
S = input()


def judge(S):
    for i in range(len(S)):
        if (i == A and S[i] != "-")or (i != A and S[i] == "-"):
            return "No"
    return "Yes"


print(judge(S))
