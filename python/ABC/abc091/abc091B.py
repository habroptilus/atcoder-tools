N = int(input())
s = []
for i in range(N):
    s.append(input().split())
M = int(input())
t = []
for i in range(M):
    t.append(input().split())

max_gain = 0
for i in range(N):
    blue = len([s[j] for j in range(N) if s[j] == s[i]])
    red = len([t[j] for j in range(M) if t[j] == s[i]])
    max_gain = max(max_gain, blue - red)

print(max_gain)
