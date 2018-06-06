s = list(input())
t = list(input())
s.sort()
t.sort()
t.reverse()
s = "".join(s)
t = "".join(t)
if s < t:
    print("Yes")
else:
    print("No")
