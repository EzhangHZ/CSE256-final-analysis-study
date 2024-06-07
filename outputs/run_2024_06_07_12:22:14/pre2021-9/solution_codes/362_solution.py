for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    mistakes = list(map(int, input().split()))
    
    ans = [0]*26
    
    for i in range(26):
        count = 0
        for j in range(m-1):
            if mistakes[j] <= i+1:
                count += 1
        ans[ord(s[i]) - ord('a')] = m - count
    
    print(*ans)