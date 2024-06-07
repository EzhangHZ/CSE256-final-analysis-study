for case in range(int(input())):
    n, x = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    
    leaf_nodes = set()
    for u, v in edges:
        if u == x or v == x:
            leaf_nodes.add(u)
            leaf_nodes.add(v)
    
    if n % 2 == 1 and (x == 1 or x in leaf_nodes):
        print("Ayush")
    else:
        print("Ashish")