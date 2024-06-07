for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    unique_elements = set()
    ops_needed = 0
    
    for num in a:
        if num > n or num in unique_elements:
            ops_needed += 1
        unique_elements.add(num)
    
    if len(unique_elements) == n:
        print(ops_needed)
    else:
        print(-1)