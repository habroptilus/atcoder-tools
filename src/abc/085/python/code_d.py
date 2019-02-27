N, H = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_a = max(A)
filtered = [b_i for b_i in B if b_i > max_a]
sum_b = sum(filtered)
if sum_b <= H:
    print(-(-(H - sum_b) // max_a) + len(filtered))
else:
    filtered.sort()
    filtered.reverse()
    s = 0
    for i in range(len(filtered)):
        s += filtered[i]
        if s >= H:
            print(i + 1)
            break
