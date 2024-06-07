for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    operations_needed = 0
    for i in range(n-1):
        if a[i] > b[i]:
            a[i], a[i+1] = a[i+1], a[i]
            operations_needed += 1
    
    print(operations_needed)