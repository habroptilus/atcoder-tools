y, m, d = map(int, input().split("/"))
if y >= 2020:
    print("TBD")
elif y <= 2018:
    print("Heisei")
elif m >= 5:
    print("TBD")
else:
    print("Heisei")
