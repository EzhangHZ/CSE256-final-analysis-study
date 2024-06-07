import math

# Function to check if reducing half or more elements by k leaves at least half of them equal
def check_valid_k(arr, k):
    n = len(arr)
    count = 0
    for num in arr:
        if num < k:
            count += 1
    return count >= math.ceil(n/2)

# Loop through test cases
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_k = -1
    max_val = max(map(abs, arr))

    # Find the maximum possible k
    for k in range(1, max_val + 1):
        if check_valid_k(arr, k):
            max_k = k
    
    print(max_k)