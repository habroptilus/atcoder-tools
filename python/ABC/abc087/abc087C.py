N = int(input())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))

candies = A[0][0] + sum(A[1])
max_candies = candies
for i in range(N - 1):
    candies = candies + A[0][i + 1] - A[1][i]
    max_candies = max(max_candies, candies)

print(max_candies)
