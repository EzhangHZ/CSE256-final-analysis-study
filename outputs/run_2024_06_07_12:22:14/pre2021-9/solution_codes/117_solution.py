# Solution Code:

t = int(input())
for _ in range(t):
    k = int(input())
    s = input().strip()
    
    last_moment = 0
    for i in range(k-1, -1, -1):
        if s[i] == "A":
            last_moment = max(last_moment, i+1)
    
    print(last_moment)