
def get_t_score(a, t_i):
    max_a = -10000000000000
    score = 0
    for a_i in range(len(a)):
        if a_i == t_i:
            continue
        if a_i > t_i:
            T = a[t_i:a_i + 1]
        else:
            T = a[a_i:t_i + 1]
        score_t, score_a = calc_scores(T)
        if max_a < score_a:
            score = score_t
            max_a = score_a
    return score


def calc_scores(T):
    aoki = sum([T[i] for i in range(len(T)) if i % 2 == 1])
    takahashi = sum([T[i] for i in range(len(T)) if i % 2 == 0])
    return takahashi, aoki


N = int(input())
a = list(map(int, input().split()))


ans = -10000000000000
for t_i in range(N):
    t_score = get_t_score(a, t_i)
    ans = max(t_score, ans)

print(ans)
