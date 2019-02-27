N = int(input())
S = input()
max_count = 0
for i in range(1, N):
    X = set(list(S[:i]))
    Y = S[i:]
    count = 0
    for c in X:
        if c in Y:
            count += 1
    max_count = max(max_count, count)
print(max_count)
