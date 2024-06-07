MOD = 10**9 + 7

def dfs(graph, source, target, length, current):
    global count
    if length > 1:
        return
    
    if current == target and length <= 1:
        count += 1

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph, source, target, length + 1, neighbor)
            visited.remove(neighbor)

t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    
    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0
    visited.add(s)
    dfs(graph, s, t, 0, s)
    print(count % MOD)