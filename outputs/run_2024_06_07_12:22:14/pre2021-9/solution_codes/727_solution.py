# Read input
n = int(input())
a = list(map(int, input().split()))

# Initialize operations count
operations = 0

# First type of operation: removing range of elements
for i in range(1, n+1):
    if a[i-1] > 0:
        for j in range(i+1, n+1):
            if a[j-1] > 0:
                min_occurrence = min(a[i-1:j])
                for k in range(i, j):
                    a[k-1] -= min_occurrence
                operations += min_occurrence

# Second type of operation: removing occurrences of single element
for i in range(1, n+1):
    if a[i-1] > 0:
        operations += a[i-1]

# Output the minimum number of operations required
print(operations)