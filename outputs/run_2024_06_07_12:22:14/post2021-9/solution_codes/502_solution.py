from collections import deque

def tree_vertices_remaining(n, k, edges):
    if n == 1: # Special case when tree has only 1 vertex
        return 1 if k % 2 == 0 else 0

    adj_list = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    leaves = deque([node for node in adj_list if len(adj_list[node]) == 1])

    while k > 0 and len(leaves) > 0:
        k -= 1
        new_leaves = deque()
        
        while leaves:
            leaf = leaves.popleft()
            next_node = adj_list[leaf][0]
            adj_list[next_node].remove(leaf)
            if len(adj_list[next_node]) == 1:
                new_leaves.append(next_node)

        leaves = new_leaves

    return len(leaves)

t = int(input())
input() # Skip empty line

for _ in range(t):
    n, k = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n-1)]

    result = tree_vertices_remaining(n, k, edges)
    print(result)