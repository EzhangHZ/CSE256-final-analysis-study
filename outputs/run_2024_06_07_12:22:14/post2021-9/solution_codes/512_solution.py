# Solution Code:

for _ in range(int(input())):
    l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    xor_val = 0
    for num in a:
        xor_val ^= num
        
    print(xor_val)