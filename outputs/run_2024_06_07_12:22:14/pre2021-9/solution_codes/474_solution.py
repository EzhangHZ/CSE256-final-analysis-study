from math import ceil

# Function to find the permutation p for a test case
def find_permutation(n, k):
    p = [0] * k
    for i in range(k):
        if i < ceil(n/2):
            p[i] = k - i
        else:
            p[i] = i - k + 1
    return p

# Main code to iterate over test cases
for _ in range(int(input())):
    n, k = map(int, input().split())

    if n >= 2 * k or n < k or k > 10**5:
        continue

    p = find_permutation(n, k)
    print(*p)