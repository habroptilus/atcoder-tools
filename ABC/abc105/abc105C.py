N = int(input())

temp = N
result = []

while temp != 0:
    if temp % 2 == 0:
        ans = 0
    else:
        ans = 1
    temp = (temp - ans) // (-2)
    result.append(str(ans))
result.reverse()
if N == 0:
    print(0)
else:
    print("".join(result))
