for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_val = max(a)
    sum_val = sum(a)
    
    if (sum_val % n == 0) and (max_val <= (sum_val // n)):
        print("YES")
    else:
        print("NO")