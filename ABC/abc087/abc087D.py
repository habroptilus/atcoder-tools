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
        self.x = [None] * N
        self.N = N
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
            print("{}=>".format(i.index + 1), end="")
            while node != i:
                print("{}({})".format(node.index + 1, node.weight), end=" ")
                node = node.next
            print("")

    def _DFS(self, s_head):  # 始点sから到達できる連結成分を深さ優先探索
        node = s_head.next
        while node != s_head:
            new_x = self.x[s_head.index] + node.weight
            if self.x[node.index] is not None and self.x[node.index] != new_x:
                #print("node{}NG".format(node.index + 1))
                return False
            elif self.x[node.index] == new_x:
                pass
            else:
                #print("node{}".format(node.index + 1))
                self.x[node.index] = new_x
                return self._DFS(self.heads[node.index])
            node = node.next
        return True

    def DFS(self):  # すべての点を訪れるまで深さ優先探索
        for i in range(self.N):
            node = self.heads[i]
            if self.x[node.index] is None:
                self.x[node.index] = 0
                if not self._DFS(self.heads[node.index]):
                    return "No"
        return "Yes"


G = WDG(N, M, L, R, D)
# G.show_graph()
print(G.DFS())
