s = input()
K = int(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
result = []

for u in alphabet:
    for i in range(len(s)):
        if s[i] == u:
            for j in range(i + 1, min(i + K + 1, len(s) + 1)):
                result.append(s[i:j])
    result = list(set(result))
    if len(result) > K:
        break

result.sort()
print(result[K - 1])
