class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.components -= 1

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    dsu = DSU(n)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                dsu.union(i, j)
    print(dsu.components)