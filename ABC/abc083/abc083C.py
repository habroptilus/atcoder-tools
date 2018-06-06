X, Y = map(int, input().split())
i = 0
while X * 2**i <= Y:
    i += 1

print(i)
