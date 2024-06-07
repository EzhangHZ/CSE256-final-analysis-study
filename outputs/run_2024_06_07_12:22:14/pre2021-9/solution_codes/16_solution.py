for _ in range(int(input())):
    n = int(input())
    strengths = list(map(int, input().split()))
    strengths.sort()
    min_diff = float('inf')
    
    for i in range(1, n):
        diff = abs(max(strengths[:i]) - min(strengths[i:]))
        min_diff = min(min_diff, diff)
    
    print(min_diff)