import math

# Function to calculate the minimum number of hops needed for Rabbit to reach destination
def min_hops(n, x, favorites):
    min_hops_count = x  # Initialize minimum number of hops to x
    for a in favorites:  # Iterate through the favorite numbers
        hops = math.ceil(x / a)  # Calculate number of hops needed for current favorite number
        min_hops_count = min(min_hops_count, hops)  # Update minimum number of hops if needed
    return min_hops_count

# Main code to read input and process each test case
t = int(input())  # Read the number of test cases
for _ in range(t):
    n, x = map(int, input().split())  # Read n and x
    favorites = list(map(int, input().split()))  # Read Rabbit's favorite numbers
    min_hops_count = min_hops(n, x, favorites)  # Calculate minimum number of hops
    print(min_hops_count)  # Print the result for current test case