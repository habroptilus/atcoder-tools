S = input()
ans = 1000
target = 753
for i in range(len(S) - 2):
    cand = int(S[i:i + 3])
    ans = min(ans, abs(cand - target))
print(ans)
