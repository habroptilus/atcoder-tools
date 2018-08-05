S = input()


def judge(S):
    if S[0] != "A":
        return "WA"
    else:
        if S[2:len(S) - 1].count("C") != 1:
            return "WA"
        else:
            for i in range(1, len(S)):
                if S[i] != "C"and S[i].isupper():
                    return "WA"
            return "AC"


print(judge(S))
