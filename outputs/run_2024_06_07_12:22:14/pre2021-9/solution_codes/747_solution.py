def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def is_possible(n, m, initial, target, edges):
    parent = [i for i in range(n)]
    rank = [0] * n

    for i, j in edges:
        union(parent, rank, i-1, j-1)

    groups = {}
    for i in range(n):
        root = find(parent, i)
        if root not in groups:
            groups[root] = [initial[i], target[i]]
        else:
            groups[root][0] += initial[i]
            groups[root][1] += target[i]

    for group in groups.values():
        if group[0] != group[1]:
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    initial = list(map(int, input().split()))
    target = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    result = is_possible(n, m, initial, target, edges)
    print(result)