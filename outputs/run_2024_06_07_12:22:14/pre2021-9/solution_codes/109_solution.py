for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    steps = 0
    sum_a = sum(a)
    product_a = 1
    for num in a:
        product_a *= num
    
    if sum_a == 0 or product_a == 0:
        steps += 1
        
        if all(num == 0 for num in a):
            steps += 1
            a[0] += 1
        else:
            if sum_a == 0:
                a[a.index(max(a))] += 1
            if product_a == 0:
                a[a.index(max(a))] += 1
                
    print(steps)