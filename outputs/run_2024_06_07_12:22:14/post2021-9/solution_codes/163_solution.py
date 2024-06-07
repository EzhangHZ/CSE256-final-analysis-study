MOD = 998244353

# Function to calculate the number of beautiful permutations
def beautiful_permutations(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Calculate the number of beautiful permutations using combinatorics
        ans = 1
        for i in range(2, n+1):
            ans = (ans * i) % MOD
        return ans

# Main code to handle test cases
t = int(input())
for _ in range(t):
    n = int(input())
    result = beautiful_permutations(n)
    print(result)