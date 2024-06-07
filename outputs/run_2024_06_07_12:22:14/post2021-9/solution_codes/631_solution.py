# Read the integer n
n = int(input())

# Read the sequence of integers a1, a2, ..., an
a = list(map(int, input().split()))

# Initialize shots to keep track of total number of onager shots needed
shots = 0

# If there are only 2 sections in the wall
if n == 2:
    print(2)
else:
    # Loop through the sections from the second to the second-to-last section
    for i in range(1, n-1):
        # Calculate number of shots needed to break current section and adjacent sections
        shots += max(0, a[i] - a[i-1] - a[i+1] + 1)

    # Print the total shots needed
    print(shots)