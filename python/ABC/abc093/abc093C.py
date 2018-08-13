A, B, C = map(int, input().split())
min_v, med_v, max_v = sorted([A, B, C])
count = 0
i = 0
while i != 10:
    i += 1
    #print(max_v, med_v, min_v, count)
    if min_v == med_v and med_v == max_v:
        print(count)
        break
    elif min_v != med_v and med_v != max_v and max_v != min_v:
        count += max_v - med_v
        min_v += max_v - med_v
        med_v = max_v
    elif min_v == med_v:
        count += max_v - med_v
        min_v = max_v
        med_v = max_v
    elif med_v == max_v and max_v - min_v != 1:
        count += int((max_v - min_v) / 2)
        min_v += int((max_v - min_v) / 2) * 2
    else:
        count += 1
        min_v = max_v
        max_v += 1
