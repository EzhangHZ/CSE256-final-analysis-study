from collections import defaultdict

def count_paths(graph, start, end, visited):
    if start == end:
        return 1
    if visited[start] == 1:
        return -1
    if visited[start] == 2:
        return 0
    
    visited[start] = 1
    paths = 0
    for neighbor in graph[start]:
        result = count_paths(graph, neighbor, end, visited)
        if result == -1:
            visited[start] = 2
            return -1
        paths += result
    
    visited[start] = 2
    return paths

for _ in range(int(input())):
    input()  # Read and discard the empty line
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    for v in range(1, n+1):
        visited = [0] * (n + 1)
        result = count_paths(graph, 1, v, visited)
        print(result, end=" ")
    
    print()