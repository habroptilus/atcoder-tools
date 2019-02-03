N = int(input())
L = list(map(int, input().split()))

if sum(L) > 2 * max(L):
    print("Yes")
else:
    print("No")
