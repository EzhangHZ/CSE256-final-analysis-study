import sys

sys.setrecursionlimit(10**6)

def dfs(node, parent, adj_list, industry_cities, happiness, tourism_cities):
    tourism_cities[node] = 1
    for child in adj_list[node]:
        if child == parent:
            continue
        dfs(child, node, adj_list, industry_cities, happiness, tourism_cities)
        if child in industry_cities:
            happiness[node] += happiness[child]
            tourism_cities[node] += tourism_cities[child]

n, k = map(int, input().split())

adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

industry_cities = set(map(int, input().split()))

happiness = [1] * (n+1)
tourism_cities = [0] * (n+1)

dfs(1, 0, adj_list, industry_cities, happiness, tourism_cities)

extra_cities = n - k
happiness_diff = [tourism_cities[i] - happiness[i] for i in range(1, n+1)]
happiness_diff.sort(reverse=True)

print(sum(happiness_diff[:extra_cities]))