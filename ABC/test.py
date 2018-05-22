s = input()
K = int(input())
subs = []
for i in range(0, len(s)):
    for j in range(i + 1, K + i + 1 if i + K <= len(s) else len(s) + 1):
        subs.append(s[i:j])
subs = list(set(subs))
subs.sort()
print(subs[K - 1])
