def is_palindrome_path(u, v, m, graph):
    if m % 2 != 0:
        return False
    for k in range(len(graph)):
        if graph[u][k] == graph[v][k] and graph[v][k] != '*':
            return True
    return False

def find_palindrome_path(n, m, edges):
    for u in range(n):
        for v in range(n):
            if u != v and is_palindrome_path(u, v, m, edges): 
                return True, [u+1, v+1]
    return False, []

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = [list(input().strip()) for _ in range(n)]
    
    found, path = find_palindrome_path(n, m, edges)
    if found:
        print("YES")
        print(" ".join(map(str, path)))
    else:
        print("NO")