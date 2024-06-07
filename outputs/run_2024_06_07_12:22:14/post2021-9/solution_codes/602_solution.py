# Solution Code:

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    for _ in range(n-1):
        b = [a[i+1]-a[i] for i in range(n-1)]
        b.sort()
        a = b
        n -= 1
        
    print(a[0])