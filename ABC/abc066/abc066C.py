N = int(input())
a = list(map(int, input().split()))


if N % 2 == 1:
    b = [a[i] for i in range(len(a)) if i % 2 == 0][::-1]
    c = [a[i] for i in range(len(a)) if i % 2 == 1]
    ans = list(map(str, b + c))
    print(" ".join(ans))
else:
    b = [a[i] for i in range(len(a)) if i % 2 == 1][::-1]
    c = [a[i] for i in range(len(a)) if i % 2 == 0]
    ans = list(map(str, b + c))
    print(" ".join(ans))
