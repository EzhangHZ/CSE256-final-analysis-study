n = int(input())
max_jump_heights = list(map(int, input().split()))
slip_distances = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0
prev_height = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if j + max_jump_heights[j] >= i:
            if dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1
                prev_height[i] = j

if dp[n] == float('inf'):
    print(-1)
else:
    jumps = []
    while n > 0:
        jumps.append(n)
        n = prev_height[n]

    jumps.reverse()
    print(dp[-1])
    print(" ".join(map(str, jumps)))