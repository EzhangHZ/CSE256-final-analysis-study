for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    found = False
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 10 == 3:
                    found = True
                    break
            if found:
                break
        if found:
            break
    
    if found:
        print("YES")
    else:
        print("NO")