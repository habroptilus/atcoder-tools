D, G = map(int, input().split())
P = []
C = []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)


def bit_search(A):
    result = []
    for i in range(1 << len(A)):
        output = []
        for j in range(len(A)):
            if ((i >> j) & 1) == 1:
                output.append(A[j])
        result.append(output)

    return result


search_list = bit_search(list(range(D)))
ans = 10 ** 9
for complete_list in search_list:
    score = sum([100 * (i + 1) * P[i] + C[i] for i in complete_list])
    count = sum([P[i] for i in complete_list])
    if score >= G:
        ans = min(ans, count)
    else:
        j_max = max([i for i in range(D) if i not in complete_list])
        required = -(-(G - score) // (100 * (j_max + 1)))
        if required < P[j_max]:
            count += required
            ans = min(ans, count)
print(ans)
