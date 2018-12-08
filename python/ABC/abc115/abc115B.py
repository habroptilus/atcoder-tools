N = int(input())
p = [int(input()) for _ in range(N)]

print(sum(p) - max(p) // 2)
