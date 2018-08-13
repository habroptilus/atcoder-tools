N = int(input())
S = list(input())

count = len([s for s in S[1:] if s == "E"])
min_count = count
for i in range(1, N):
    if S[i - 1] == "W":
        count += 1
    if S[i] == "E":
        count -= 1
    min_count = min(min_count, count)
print(min_count)
