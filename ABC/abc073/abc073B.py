N = int(input())
s = 0
for i in range(N):
    l, r = map(int, input().split())
    s += r - l + 1
print(s)
