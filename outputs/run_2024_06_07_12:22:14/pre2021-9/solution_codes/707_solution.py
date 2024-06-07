for _ in range(int(input())):
    n, k = map(int, input().split())
    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())
    
    I = (min(r1, r2) - max(l1, l2)) * n
    
    if I >= k:
        print(0)
    else:
        steps = k - I
        print(steps)