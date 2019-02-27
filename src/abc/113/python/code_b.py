N = int(input())
T, A = map(int, input().split())
H = map(int, input().split())

t = [T - h * 0.006 for h in H]
ans = 10**9
for i in range(len(t)):
    if abs(t[i] - A) < ans:
        ans_i = i
        ans = abs(t[i] - A)
print(ans_i + 1)
