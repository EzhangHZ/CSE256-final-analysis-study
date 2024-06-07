import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent=None, depth=0):
    global min_steps
    if node in seq_1:
        steps = abs(depth - seq_1[node])
    elif node in seq_2:
        steps = abs(depth - seq_2[node])

    min_steps = max(min_steps, steps)
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth+1)

n, d = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

m1, *seq_1 = map(int, input().split())
m2, *seq_2 = map(int, input().split())

min_steps = 0
dfs(1)

print(min_steps * 2)