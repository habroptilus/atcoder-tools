N = int(input())
A = []
B = []
S = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    S.append((i, a + b))
ans = 0
S.sort(key=lambda x: x[1], reverse=True)
for i in range(N):
    if i % 2 == 0:
        ans += A[S[i][0]]
    else:
        ans -= B[S[i][0]]

print(ans)
