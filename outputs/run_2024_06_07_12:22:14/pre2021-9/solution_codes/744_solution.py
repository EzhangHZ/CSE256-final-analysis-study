n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    
    diff = [b[i] - a[i] for i in range(n)]
    
    total_diff = sum(diff[l-1:r])
    
    if total_diff != 0:
        if total_diff % 2 == 0:
            print((total_diff//2) + 1)
        else:
            print("-1")
    else:
        count = 0
        for i in range(l-1, r):
            if diff[i] < 0:
                count += abs(diff[i])
        print(count)