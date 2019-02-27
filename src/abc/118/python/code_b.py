N, M = map(int, input().split())
likes = [0] * M
for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)):
        likes[temp[i] - 1] += 1
print(len([e for e in likes if e == N]))
