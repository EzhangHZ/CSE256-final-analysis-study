MOD = 998244353

# Function to calculate the number of non-empty MEX-correct subsequences
def mex_correct_subsequences(n, a):
    dp = [0] * (n + 1)
    mex = 0
    for i in range(n):
        dp[i + 1] = (2 * dp[i] - dp[a[i]] + 2) % MOD
        mex = max(mex, dp[a[i]])
    result = (dp[n] - mex) % MOD
    return result

# Main code
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = mex_correct_subsequences(n, a)
    print(result)