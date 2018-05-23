N, C = map(int, input().split())
x = [0]
v = [0]
for _ in range(N):
    x_new, v_new = map(int, input().split())
    x.append(x_new)
    v.append(v_new)


def get_g(clockwise):
    g = []
    g_now = 0
    g.append(g_now)
    if clockwise:
        for i in range(1, N + 1):
            g_next = g_now + v[i] + x[i - 1] - x[i]
            g.append(g_next)
            g_now = g_next
    else:
        for i in range(1, N + 1):
            g_next = g_now + v[i] + 2 * x[i - 1] - 2 * x[i]
            g.append(g_next)
            g_now = g_next
    return g


def get_h(clockwise):
    h = []
    if clockwise:
        h_now = v[N] - 2 * (C - x[N])
        h.append(h_now)
        for i in range(N):
            h_next = v[N - i - 1] + h_now + 2 * (x[N - i - 1] - x[N - i])
            h.append(h_next)
            h_now = h_next
    else:
        h_now = v[N] - C + x[N]
        h.append(h_now)
        for i in range(N):
            h_next = v[N - i - 1] + h_now + x[N - i - 1] - x[N - i]
            h.append(h_next)
            h_now = h_next
    h = list(reversed(h))
    return [0] + h[1:]


def get_G(g):
    G = []
    max_g = -100000000
    for i in range(N + 1):
        max_g = max(max_g, g[i])
        G.append(max_g)
    return [G[-1]] + G[:-1]


answer = 0
for clockwise in [True, False]:
    g = get_g(clockwise)
    h = get_h(clockwise)
    G = get_G(g)
    answer = max(max([G[b] + h[b] for b in range(N + 1)]), answer)

print(answer)
