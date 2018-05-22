s = input()
K = int(input())
result = []
for i in range(len(s)):
    for j in range(i + 1, min(i + K + 1, len(s) + 1)):
        result.append(s[i:j])

result = list(set(result))
result.sort()
# print(result)
# print(len(result))
print(result[K - 1])
