for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = input()
    b = input()
    
    if a == b:
        print(0)
        continue
        
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + x
        
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + y)
        
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + y)
            
        if i >= 4:
            dp[i] = min(dp[i], dp[i - 4] + y)
            
        if a[i-1] != b[i-1]:
            dp[i] = min(dp[i], dp[i-1])
        
    if dp[n] >= 10**9:
        print(-1)
    else:
        print(dp[n])