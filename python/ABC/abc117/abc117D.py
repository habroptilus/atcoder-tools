N, K = map(int, input().split())
A = list(map(int, input().split()))

binary = [bin(a) for a in A]
bin_K = bin(K)
ma_len = max([len(e) for e in binary] + [len(bin_K)]) - 2
B = [e[2:].zfill(ma_len) for e in binary]
bin_K = bin_K[2:].zfill(ma_len)
ans = 0
X = []

flag = False
for i in range(ma_len):
    num_1 = 0
    num_0 = 0
    for j in range(N):
        if B[j][i] == "0":
            num_0 += 1
        else:
            num_1 += 1
    if num_1 >= num_0:
        added = "0"
        if bin_K[i] == "1":
            flag = True
    else:
        if flag:
            added = "1"
        else:
            if bin_K[i] == "1":
                added = "1"
            else:
                added = "0"
    if added == "1":
        ans += 2**(ma_len - i - 1) * num_0
    else:
        ans += 2**(ma_len - i - 1) * num_1
    # X.append(added)

print(ans)
# print("".join(X))
