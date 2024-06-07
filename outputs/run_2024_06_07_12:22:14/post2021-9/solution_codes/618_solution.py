# Function to find a pair of substrings that satisfy the conditions of the query
def find_substrings(s, w, l, r, k):
    n = len(s)
    MOD = 9
    pow10 = [1] * (n+1)
    for i in range(1, n+1):
        pow10[i] = (pow10[i-1] * 10) % MOD
    
    v_lr = lambda l, r: int(s[l-1:r])  # Numeric value of substring s[l:r]
    
    for L1 in range(1, n-w+2):
        if l <= L1 <= r:  # Ensure L1, L2 are not part of the query substring
            continue
        for L2 in range(L1+1, n-w+2):
            if l <= L2 <= r:  # Ensure L1, L2 are not part of the query substring
                continue
            if (v_lr(L1, L1+w) * v_lr(l, r+1) + v_lr(L2, L2+w)) % MOD == k:
                return L1, L2
    return -1, -1

t = int(input())  # Number of test cases
for _ in range(t):
    s = input().strip()  # Input string
    n = len(s)
    w, m = map(int, input().split())  # Substring length and number of queries
    for _ in range(m):
        l, r, k = map(int, input().split())  # Query parameters
        L1, L2 = find_substrings(s, w, l, r, k)
        print(f"{L1} {L2}")