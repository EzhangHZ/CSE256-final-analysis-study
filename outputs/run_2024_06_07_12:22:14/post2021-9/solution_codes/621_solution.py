for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    
    if len(set(b)) < len(b):
        print(-1)
        continue
    
    p = [0] * n
    p[0] = 1
    
    for i in range(1, n//2):
        p[2*i-1] = b[i-1]
        p[2*i] = 0
        
    b_min = min(b)
    
    for i in range(1, n//2):
        if p[2*i] == 0:
            next_num = b_min + 1
            while next_num in p:
                next_num += 1
            p[2*i] = next_num
            
    print(" ".join(map(str, p)))