from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    l, r, d = map(int, input().split())
    G[l - 1].append((r - 1, d))
    G[r - 1].append((l - 1, -d))
q = deque()

x = [None] * N


def _BFS(start):
    q.append(start)
    while len(q) != 0:
        p = q.popleft()
        for index, d in G[p]:
            if x[index] is None:
                x[index] = x[p] + d
                q.append(index)
            elif x[index] != x[p] + d:
                return False
    return True


def BFS():
    for i in range(N):
        if x[i] is None:
            x[i] = 0
            if not _BFS(i):
                return "No"
    return "Yes"


print(BFS())

# 以下、最初に実装してTLEになったクラス
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
        self.q = deque()
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
            if self.x[node.index] is None:
                print("node{}".format(node.index + 1))
                self.x[node.index] = new_x
                if not self._DFS(self.heads[node.index]):
                    return False
            elif self.x[node.index] != new_x:
                print("node{}NG".format(node.index + 1))
                return False
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

    def _BFS(self, s_head):
        self.q.append(s_head)
        while len(self.q) != 0:
            p = self.q.popleft()
            node = p.next
            while node != p:
                if self.x[node.index] is None:
                    self.x[node.index] = self.x[p.index] + node.weight
                    self.q.append(self.heads[node.index])
                elif self.x[node.index] != self.x[p.index] + node.weight:
                    return False
                node = node.next
        return True

    def BFS(self):
        for i in range(self.N):
            node = self.heads[i]
            if self.x[i]is None:
                self.x[i] = 0
                if not self._BFS(node):
                    return "No"
        return "Yes"
