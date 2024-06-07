for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    w = s[:n-1] + s[-1]
    print(w)