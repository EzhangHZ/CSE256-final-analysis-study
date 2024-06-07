# Solution Code:

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    min_length = float('inf')
    found = False
    
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub_str = s[i:j]
            count_a = sub_str.count('a')
            count_b = sub_str.count('b')
            count_c = sub_str.count('c')
            
            if count_a > count_b and count_a > count_c:
                min_length = min(min_length, j - i)
                found = True
    
    if found:
        print(min_length)
    else:
        print(-1)