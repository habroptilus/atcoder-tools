c = []
for i in range(3):
    c.append(input())

print("".join([c[i][i] for i in range(3)]))
