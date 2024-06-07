for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    s = set(range(1, k+1))
    
    d1 = {}  # tracks position of cards at the start
    d2 = {}  # tracks position of cards at the end
    
    for i in range(k):
        d1[a[i]] = (1, 1) if a[i] == 1 else None
        d2[a[i]] = (n, m) if a[i] == k else None
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(2, k+1):
        r, c = d1[i]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= n and 1 <= nc <= m and d1.get(i+1) == (nr, nc):
                d1[i], d1[i+1] = d1[i+1], d1[i]
                break
                
    for i in range(k, 1, -1):
        r, c = d2[i]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= n and 1 <= nc <= m and d2.get(i-1) == (nr, nc):
                d2[i], d2[i-1] = d2[i-1], d2[i]
                break
    
    valid = all(d1[i] and d2[i] for i in range(1, k+1))
    
    if valid:
        print("YA")
    else:
        print("TIDAK")