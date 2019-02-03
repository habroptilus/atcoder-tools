# 嘘解法なおそうとおもったけどなおらん。
N, K = map(int, input().split())
A = list(map(int, input().split()))

binary = [bin(a) for a in A]
bin_K = bin(K)
ma_len = max([len(e) for e in binary] + [len(bin_K)]) - 2
B = [e[2:].zfill(ma_len) for e in binary]
bin_K = bin_K[2:].zfill(ma_len)
ans = 0
X = []


def latter(div, ma_len, B, bin_K):
    result = 0
    for i in range(div, ma_len):
        num_0 = 0
        num_1 = 0
        for j in range(len(B)):
            if B[j][i] == "0":
                num_0 += 1
            else:
                num_1 += 1
        result += 2**(ma_len - i - 1) * max(num_0, num_1)
    return result


ans = 0
former = 0
for i in range(ma_len):
    if bin_K[i] == "1":
        med = 2**(ma_len - i - 1) * len([B[j][i]
                                         for j in range(N) if B[j][i] == "1"])
        rest = latter(i + 1, ma_len, B, bin_K)
        ans = max(ans, former + med + rest)

        former += 2**(ma_len - i - 1) * len([B[j][i]
                                             for j in range(N) if B[j][i] == "0"])
    else:
        former += 2**(ma_len - i - 1) * len([B[j][i]
                                             for j in range(N) if B[j][i] == "1"])
if ans == 0:
    ans = former
print(ans)
