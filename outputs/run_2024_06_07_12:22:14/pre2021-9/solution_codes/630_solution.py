# Solution Code:

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] == arr[k] and arr[j] == arr[l]:
                        count += 1

    print(count)