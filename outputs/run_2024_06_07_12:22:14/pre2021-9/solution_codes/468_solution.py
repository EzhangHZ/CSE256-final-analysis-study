from collections import defaultdict

def dfs(node, parent):
    global label
    for child in tree[node]:
        if child != parent:
            label = (label + 1) % (n - 1)
            labels[(min(node, child), max(node, child))] = label
            dfs(child, node)

n = int(input())
tree = defaultdict(list)
labels = {}
label = 0

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1, 0)

for i in range(n - 1):
    print(labels[(min(i + 1, i + 2), max(i + 1, i + 2))])