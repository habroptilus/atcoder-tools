S = input()
i = 2
while True:
    if S[:(len(S) - i) // 2] * 2 == S[:len(S) - i]:
        print(len(S) - i)
        break
    i += 2
