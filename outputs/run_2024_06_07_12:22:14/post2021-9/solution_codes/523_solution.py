class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]


n, d = map(int, input().split())
dsu = DSU(n)
conditions = [tuple(map(int, input().split())) for _ in range(d)]

max_acquaintances = [0] * d

for i in range(d):
    x, y = conditions[i]
    dsu.union(x-1, y-1)

    max_acquaintances[i] = max(max_acquaintances[i-1], len(set(dsu.find(j) for j in range(n)))

for num in max_acquaintances:
    print(num)