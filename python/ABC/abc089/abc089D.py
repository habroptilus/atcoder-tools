# 累積和Xを計算するときに余りの値ごとにグループを作っている(２次元配列になっている)けど、
# そんなことする必要はなく、単純に一次元配列にしてX[i]に先頭からDずつ進めた時に到達できたとして
# かかるコストを格納すればよかった。いつかかきなおす
H, W, D = map(int, input().split())
A = [0] * H * W
for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        A[temp[j] - 1] = (i + 1, j + 1)

Q = int(input())
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


def consumption(point_A, point_B):
    return abs(point_A[0] - point_B[0]) + abs(point_A[1] - point_B[1])


X = []
for i in [D] + list(range(1, D)):
    power = 0
    x = [0]
    for j in range(int((H * W - i) / D)):
        power += consumption(A[i - 1 + j * D], A[i - 1 + (j + 1) * D])
        x.append(power)
        #print("{}->{}".format(A[i - 1], A[i - 1 + (j + 1) * D]))
    X.append(x)
# print(X)
for i in range(Q):
    k = L[i] % D
    if k == 0:
        l = int((L[i] - D) / D)
        r = int((R[i] - D) / D)
    else:
        l = int((L[i] - k) / D)
        r = int((R[i] - k) / D)
    #print(X[k], l, r)
    print(X[k][r] - X[k][l])
