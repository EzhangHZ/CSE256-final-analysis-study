for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if n == 1:
        print(0)
        continue
    if n == 2:
        print(min(2, m))
        continue
    
    ans = min(m, 2 * (m - 1))
    print(ans)