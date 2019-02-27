N = int(input())
points = [(0, 0)]
T = [0]
for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    points.append((x, y))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def judge(T, points, N):
    for i in range(N):
        delta_t = T[i + 1] - T[i]
        d = distance(points[i + 1], points[i])
        if not (delta_t >= d and (delta_t - d) % 2 == 0):
            return "No"
    return "Yes"


print(judge(T, points, N))
