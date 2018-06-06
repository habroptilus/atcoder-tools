a, b = map(int, input().split())
c = int(str(a) + str(b))

for i in range(c):
    if i**2 == c:
        print("Yes")
        break
    elif i**2 > c:
        print("No")
        break
