s = input().rstrip()
k = int(input())
candidates = set()
if len(s) < k:
    print(0)
else:
    for i in range(len(s) - k + 1):
        candidates.add(s[i:i + k])
    print(len(candidates))
