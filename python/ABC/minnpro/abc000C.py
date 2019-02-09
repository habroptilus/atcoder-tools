K, A, B = map(int, input().split())
e = B - A

if e <= 2 or A >= K:
    ans = K + 1
else:
    ans = B
    count = A + 1
    while count < K:
        e_count = min(ans // A, (K - count) // 2)
        if e_count > 0:
            ans += e_count * e
            count += e_count * 2
        else:
            if A > ans:
                count += min(A - ans, K - count)
                ans += min(A - ans, K - count)
            else:
                tataku = K - count
                count += tataku
                ans += tataku
print(ans)
