# Solution Code:

for _ in range(int(input())):
    n, H = map(int, input().split())
    damages = list(map(int, input().split()))
    
    count = 0
    last_weapon = None
    
    for damage in damages:
        if last_weapon == damage:
            count += 1
            last_weapon = None
        else:
            last_weapon = damage
    
    if last_weapon is not None:
        count += 1
        
    print(count)