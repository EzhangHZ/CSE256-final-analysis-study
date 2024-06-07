MOD = 10**9 + 7

def coziness(t, test_cases):
    for _ in range(t):
        n, m = test_cases[_][0], test_cases[_][1]
        segments = test_cases[_][2:]

        bitmask = [0] * n
        for segment in segments:
            l, r, x = segment
            for i in range(l-1, r):
                bitmask[i] |= x

        coziness_val = sum(bitmask) % MOD
        print(coziness_val)

# Test Input
t = 3
test_cases = [
    [2, 1, [1, 2, 2]],
    [3, 2, [1, 3, 5], [2, 3, 5]],
    [5, 4, [1, 2, 7], [3, 3, 7], [4, 4, 0], [4, 5, 2]]
]

# Calling the function to calculate and print coziness values
coziness(t, test_cases)