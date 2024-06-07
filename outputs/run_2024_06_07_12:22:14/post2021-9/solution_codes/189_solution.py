for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    operations = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            diff = a[i-1] - a[i]
            operations += diff
            a[i] = a[i-1]
    
    print(operations)