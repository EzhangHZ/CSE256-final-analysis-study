for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_beauty = 0
    
    for l in range(n):
        for r in range(l+2, n):
            max_beauty = max(max_beauty, (max(a[:l] + a[r:]) - min(a[:l] + a[r:]) + max(a[l:r]) - min(a[l:r])))
    
    print(max_beauty)