from collections import defaultdict

def is_passable_tree(graph, nodes):
    def dfs(node, parent):
        for neighbor in graph[node]:
            if neighbor != parent and neighbor in nodes:
                nodes.remove(neighbor)
                dfs(neighbor, node)

    start_node = nodes[0]
    dfs(start_node, -1)

    return len(nodes) == 0

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = int(input())
for _ in range(q):
    k = int(input())
    nodes = list(map(int, input().split()[1:])
    if is_passable_tree(graph, set(nodes)):
        print("YES")
    else:
        print("NO")