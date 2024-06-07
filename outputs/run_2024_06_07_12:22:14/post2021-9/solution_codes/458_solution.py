for _ in range(int(input())):
    n = int(input())
    weights = list(map(int, input().split()))
    weights.sort()
    
    if n % 2 == 1:
        score = abs(weights[n//2 + 1] - weights[n//2]) + abs(weights[n//2] - weights[n//2 - 1])
    else:
        score = abs(weights[n//2] - weights[n//2 - 1]) + abs(weights[n//2 + 1] - weights[n//2])
        
    print(score)