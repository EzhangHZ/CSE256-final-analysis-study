for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [-1] + [0]*n
    
    remaining = []
    for i in range(1, n+1):
        if a[i-1] != i:
            b[i] = a[i-1]
        else:
            remaining.append(i)
    
    for i in range(len(remaining)):
        if b[remaining[i]] == remaining[(i+1) % len(remaining)]:
            b[remaining[i]] = remaining[(i+2) % len(remaining)]
    
    fulfilled = sum([1 for i in range(1, n+1) if b[i] == a[i-1]])
    
    print(fulfilled)
    print(' '.join(map(str, b[1:])))