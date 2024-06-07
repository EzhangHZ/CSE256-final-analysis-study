for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    last_occurrence = {}
    l, r, l_max, r_max = 0, 0, 0, 0
    c_max = 0
    
    for i in range(n):
        if a[i] in last_occurrence:
            l = max(l, last_occurrence[a[i]] + 1)
        last_occurrence[a[i]] = i
        
        c_lr = len(set(a[l:i+1]))
        if i - l - c_lr > r_max - l_max - c_max:
            l_max, r_max, c_max = l, i, c_lr
    
    print(l_max+1, r_max+1)