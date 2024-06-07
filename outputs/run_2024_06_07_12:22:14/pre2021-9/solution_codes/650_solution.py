from collections import defaultdict

n, m, k = map(int, input().split())
special_fields = set(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, end):
    stack = [(start, 0)]
    visited = set()
    while stack:
        node, dist = stack.pop()
        visited.add(node)
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, dist + 1))
    
max_shortest_path = dfs(1, n)

max_additional_path = 0
for sf1 in special_fields:
    for sf2 in special_fields:
        if sf1 != sf2:
            graph[sf1].append(sf2)
            graph[sf2].append(sf1)
            max_additional_path = max(max_additional_path, dfs(1, n))
            graph[sf1].remove(sf2)
            graph[sf2].remove(sf1)

print(max(max_shortest_path, max_additional_path))