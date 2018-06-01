N, M = map(int, input().split())
L = []
R = []
D = []
for i in range(M):
    l, r, d = map(int, input().split())
    L.append(l)
    R.append(r)
    D.append(d)

inf = float("inf")


class WDG():  # 重み付き有向グラフ(隣接リスト表現)
    class node():
        def __init__(self, index=0, weight=0, next=None):
            self.index = index
            self.weight = weight
            self.next = next

    def __init__(self, N, M, L, R, D):
        self.heads = []
        for i in range(N):
            head = WDG.node()
            head.next = head
            head.index = i
            self.heads.append(head)
        for i in range(M):
            new1 = WDG.node(R[i] - 1, D[i], head)
            new2 = WDG.node(L[i] - 1, -D[i], head)
            self.insert(L[i] - 1, new1)
            self.insert(R[i] - 1, new2)

    def insert(self, start, new):
        new.next = self.heads[start].next
        self.heads[start].next = new

    def show_graph(self):
        for i in self.heads:
            node = i.next
            while node != i:
                print("{}({})".format(node.index + 1, node.weight), end=" ")
                node = node.next
            print("")


hoge = WDG(N, M, L, R, D)
hoge.show_graph()
