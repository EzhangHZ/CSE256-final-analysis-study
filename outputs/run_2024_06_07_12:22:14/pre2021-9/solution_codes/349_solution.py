# Read the number of test cases
for _ in range(int(input())):
    # Read the number of mountains and length of the door
    n, k = map(int, input().split())
    
    # Read the heights of mountains
    heights = list(map(int, input().split()))
    
    peaks = 0
    max_parts = 0
    left_border = 0
    
    # Calculate the number of peaks for each possible segment
    for i in range(n - k + 1):
        cur_peaks = sum(1 for j in range(i + 1, i + k - 1) if heights[j - 1] < heights[j] and heights[j] > heights[j + 1])
        
        # Update maximum number of parts and left border
        if cur_peaks > max_parts:
            max_parts = cur_peaks
            peaks = cur_peaks
            left_border = i + 1
            
        elif cur_peaks == max_parts:
            if i + 1 < left_border:
                left_border = i + 1
    
    print(peaks+1, left_border)  # Output the result