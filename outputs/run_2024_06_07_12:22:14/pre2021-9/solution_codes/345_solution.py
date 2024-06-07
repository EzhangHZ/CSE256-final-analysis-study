for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    
    if a >= max(n, m) and b >= n + m - max(n, m):
        print("Yes")
    else:
        print("No")