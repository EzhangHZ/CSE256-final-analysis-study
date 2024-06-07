for _ in range(int(input())):
    n = int(input())
    segments = list(map(int, input().split()))
    
    curr_min_len = float('inf')
    curr_end = 0
    
    for length in segments:
        curr_end = max(curr_end - length, curr_end + length)
        curr_min_len = min(curr_min_len, curr_end)
    
    print(curr_min_len)