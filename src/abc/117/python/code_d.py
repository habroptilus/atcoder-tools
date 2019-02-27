N, K = map(int, input().split())
A = list(map(int, input().split()))

binary = [bin(a) for a in A]
bin_K = bin(K)
ma_len = max([len(e) for e in binary] + [len(bin_K)]) - 2
B = [e[2:].zfill(ma_len) for e in binary]
bin_K = bin_K[2:].zfill(ma_len)


def greedy(C):
    result = []
    s = 0
    for i in range(len(C) - 1):
        s += C[len(C) - i - 1]["score"] * \
            max(C[len(C) - i - 1]["1"], C[len(C) - i - 1]["0"])
        result.append(s)
    return list(reversed(result)) + [0]


C = []
for i in range(ma_len):
    c = {"0": 0, "1": 0}
    for j in range(N):
        c[B[j][i]] += 1
    c["score"] = 2**(ma_len - i - 1)
    C.append(c)

latter = greedy(C)
ans = 0
former = 0
for i in range(ma_len):
    if bin_K[i] == "1":
        ans = max(ans, former + C[i]["1"] * C[i]["score"] + latter[i])
        former += C[i]["score"] * C[i]["0"]
    else:
        former += C[i]["score"] * C[i]["1"]

print(max(ans, former))
