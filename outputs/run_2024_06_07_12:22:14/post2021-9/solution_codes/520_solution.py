# Function to calculate the product of elements in an array
def product_of_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the array and the elements of the array
    n = int(input())
    arr = list(map(int, input().split()))

    # Initialize variables
    max_product = float('-inf')
    start = 0
    end = 0

    # Implement brute force approach to try all possible combinations
    for i in range(n + 1):
        for j in range(i, n + 1):
            # Calculate the product of the array elements after removing elements
            product = product_of_array(arr[i:j])

            # Update max_product and indices if a higher product is found
            if product > max_product:
                max_product = product
                start = i
                end = n - j

    # Output the indices that result in the maximum product
    print(start, end)