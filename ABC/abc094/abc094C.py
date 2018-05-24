N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

smaller_index = int((N - 1) / 2)
larger_index = smaller_index + 1
avg = (Y[smaller_index] + Y[larger_index]) / 2
for i in range(N):
    if X[i] < avg:
        print(Y[larger_index])
    else:
        print(Y[smaller_index])
