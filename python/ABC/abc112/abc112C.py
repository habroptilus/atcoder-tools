N = int(input())
X_h = []
Y_h = []
H = []
X_0 = []
Y_0 = []
for i in range(N):
    x, y, h = map(int, input().split())
    if h == 0:
        X_0.append(x)
        Y_0.append(y)
    else:
        X_h.append(x)
        Y_h.append(y)
        H.append(h)


def solve(H, X_h, Y_h, X_0, Y_0):
    for C_x in range(101):
        for C_y in range(101):
            h = H[0] + abs(X_h[0] - C_x) + abs(Y_h[0] - C_y)
            flag = True
            for i in range(1, len(X_h)):
                if h != H[i] + abs(X_h[i] - C_x) + abs(Y_h[i] - C_y):
                    flag = False
                    break
            if flag:
                for j in range(len(X_0)):
                    if h - abs(X_0[j] - C_x) - abs(Y_0[j] - C_y) > 0:
                        flag = False
                        break
                if flag:
                    return C_x, C_y, h


C_x, C_y, H = solve(H, X_h, Y_h, X_0, Y_0)
print(C_x, C_y, H)
