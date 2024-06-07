from collections import defaultdict

def dfs(node, parent, children, adj_list, vertices, dp):
    dp[node][0] = 0
    dp[node][1] = vertices[node - 1]
    
    for child in adj_list[node]:
        if child == parent:
            continue
        dfs(child, node, children, adj_list, vertices, dp)
        dp[node][0] += max(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]

    for child in children:
        dp[node][1] = max(dp[node][1], vertices[node - 1] + dp[child][0] + dp[node][0] - max(dp[child][0], dp[child][1]))

def max_k_coloring_value(t, test_cases):
    for i in range(t):
        n, vertices, edges = test_cases[i]
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        dp = [[0, 0] for _ in range(n + 1)]
        dfs(1, 0, adj_list[1], adj_list, vertices, dp)

        res = [dp[1][0] if j == 0 else max(dp[1][0], dp[1][1]) for j in range(1, n)]
        print(' '.join(map(str, res)))

# Test cases
test_cases = [
    (4, [3, 5, 4, 6], [(2, 1), (3, 1), (4, 3)]),
    (2, [21, 32], [(2, 1)]),
    (6, [20, 13, 17, 13, 13, 11], [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]),
    (4, [10, 6, 6, 6], [(1, 2), (2, 3), (4, 1)])
]

max_k_coloring_value(4, test_cases)