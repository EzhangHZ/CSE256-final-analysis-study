for _ in range(int(input())):
    k = int(input())
    
    count = 0
    num = 0
    
    while count < k:
        num += 1
        if num % 3 != 0 and str(num)[-1] != '3':
            count += 1
    
    print(num)