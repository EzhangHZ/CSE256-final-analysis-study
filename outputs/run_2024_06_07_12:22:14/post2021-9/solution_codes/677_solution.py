import sys
input = sys.stdin.readline

def dfs(node, parent, depth):
    global max_depth, ans
    if depth > max_depth:
        max_depth = depth
        ans = node
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1)

for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    max_depth = 0
    dfs(1, 0, 0)
    
    max_depth = 0
    dfs(ans, 0, 0)
    
    print(max_depth)