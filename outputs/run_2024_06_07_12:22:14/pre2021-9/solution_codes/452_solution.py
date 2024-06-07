# read input values
n = int(input())
arr = list(map(int, input().split()))

# initialize variables
count = 0

# iterate through each pair of adjacent elements
for i in range(n-1):
    if arr[i] + arr[i+1] == 0:
        count += 1

# output the minimum number of integers needed to be inserted
print(count)