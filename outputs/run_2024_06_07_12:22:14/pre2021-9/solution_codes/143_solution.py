for case in range(int(input())):
    n = int(input())
    
    m = n-1
    operations = [n]*m
    operations.append(1)
    
    print(m)
    print(" ".join(map(str, operations)))