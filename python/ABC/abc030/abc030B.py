n, m = map(int, input().split())

if n >= 12:
    n = n - 12
ang_s = n * 30 + m / 2
ang_l = m * 6
print(min(abs(ang_s - ang_l), 360 - abs(ang_s - ang_l)))
