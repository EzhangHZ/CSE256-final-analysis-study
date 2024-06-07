for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    i, j = 0, 0
    online_members = set()
    
    while i < n and j < n:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            online_members.add(a[i])
            i += 1
    
    print(len(online_members))