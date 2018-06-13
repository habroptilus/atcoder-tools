A, B, C, D, E, F = map(int, input().split())


def create_candidates(w_x, w_y, F):
    """
    >>> create_candidates(2,11,15)
    {0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15}
    """
    candidates = set()
    for x in range(F):
        if w_x * x > F:
            break
        for y in range(F):
            a = w_x * x + w_y * y
            if a <= F:
                candidates.add(a)
            else:
                break
    return candidates


candidates_a = create_candidates(100 * A, 100 * B, F)
candidates_b = create_candidates(C, D, F)
candidates_a.remove(0)

max_dense = -float("inf")
max_a = -1
max_b = -1
for a in candidates_a:
    for b in candidates_b:
        if a + b <= F and b <= a * E / 100 and 100 * b / (a + b) > max_dense:
            max_dense = 100 * b / (a + b)
            max_a = a
            max_b = b

print(max_a + max_b, max_b)
