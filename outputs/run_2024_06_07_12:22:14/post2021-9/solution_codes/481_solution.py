for _ in range(int(input())):
    n, a, b = map(int, input().split())
    kingdoms = list(map(int, input().split()))
    
    total_cost = b * (kingdoms[-1] - kingdoms[0])
    for i in range(1, n):
        total_cost = min(total_cost, a * abs(kingdoms[i] - kingdoms[i - 1]) + b * (kingdoms[i] - kingdoms[0]))
    
    print(total_cost)