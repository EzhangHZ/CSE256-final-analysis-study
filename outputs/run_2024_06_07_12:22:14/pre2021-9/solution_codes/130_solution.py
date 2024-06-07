for case in range(int(input())):
    c, d = map(int, input().split())
    diff = abs(c - d)
    
    if diff % 2:
        print("-1")
        continue
    
    if diff == 0:
        if c == 0:
            print("0")
        else:
            print("1")
        continue
    
    print("2")