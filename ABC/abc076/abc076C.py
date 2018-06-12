S = input()
T = input()
ans = "UNRESTORABLE"
if len(S) >= len(T):
    for i in range(len(S) - len(T) + 1):
        s = S[i:len(T) + i]
        for j in range(len(s)):
            if s[j] != "?" and s[j] != T[j]:
                break
            if j == len(s) - 1:
                c = S[:i] + T + S[len(T) + i:]
                ans = c.replace("?", "a")

print(ans)
