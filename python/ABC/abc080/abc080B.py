N = int(input())
f_N = sum(list(map(int, list(str(N)))))
if N % f_N == 0:
    print("Yes")
else:
    print("No")
