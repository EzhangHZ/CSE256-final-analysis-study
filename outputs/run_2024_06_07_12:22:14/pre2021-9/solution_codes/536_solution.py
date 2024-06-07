MOD = 10**9 + 7

def calculate_multiset_size(n, k):
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j % 2] = (dp[i-1][(j-1) % 2] + dp[i][j % 2]) % MOD
    
    return (dp[n][k % 2] % MOD)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    result = calculate_multiset_size(n, k)
    print(result)


This Python code reads the number of test cases, iterates through each test case, calculates the size of the multiset $S$ using dynamic programming approach, and outputs the size of the multiset modulo $10^9+7$.