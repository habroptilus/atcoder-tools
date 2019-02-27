import itertools
N, A, B, C = map(int, input().split())
target = [C, B, A]
L = []
for i in range(N):
    L.append(int(input()))

products = list(itertools.product([0, 1, 2, 3], repeat=N))

ans = float("inf")
for p in products:
    scores = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(p)):
        scores[p[i]][0] += L[i]
        scores[p[i]][1] += 1
    temp = [elem[0] for elem in scores[:3]]
    cost = sum([10 * (elem[1] - 1) for elem in scores[:3] if elem[1] >= 1])
    if 0 in temp:
        continue
    cost += sum([abs(target[i] - temp[i]) for i in range(3)])
    ans = min(ans, cost)
print(ans)
