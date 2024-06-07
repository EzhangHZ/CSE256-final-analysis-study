from collections import defaultdict, deque

def build_graph(n, r, c):
    graph = defaultdict(list)
    for i in range(n):
        graph[(r[i], c[i])].append((r[i] + 1, c[i]))  # Activated edge
        graph[(r[i], c[i])].append((r[i] + 1, c[i] + 1))  # Non-activated edge
        graph[(r[i] + 1, c[i])].append((r[i], c[i] + 1))
        graph[(r[i] + 1, c[i] + 1)].append((r[i], c[i]))
    return graph

def dijkstra(graph):
    start = (1, 1)
    end = set(graph.keys())
    distances = {node: float('inf') for node in end}
    distances[start] = 0
    visited = set()

    q = deque([start])
    while q:
        node = q.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if distances[neighbor] > distances[node] + 1:
                distances[neighbor] = distances[node] + 1
                q.append(neighbor)
    
    return min(distances.values())

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    graph = build_graph(n, r, c)
    min_cost = dijkstra(graph)
    print(min_cost)