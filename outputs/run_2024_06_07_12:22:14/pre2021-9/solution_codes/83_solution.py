for case in range(int(input())):
    px, py = map(int, input().split())
    orders = input()
    
    x, y = 0, 0
    for order in orders:
        if order == 'U':
            y += 1
        elif order == 'D':
            y -= 1
        elif order == 'R':
            x += 1
        elif order == 'L':
            x -= 1
    
    dx = px - x
    dy = py - y
    
    can_reach = True
    
    if dx > 0:
        can_reach = 'R' in orders[:dx]
    elif dx < 0:
        can_reach = 'L' in orders[:abs(dx)]
        
    if dy > 0:
        can_reach = 'U' in orders[:dy]
    elif dy < 0:
        can_reach = 'D' in orders[:abs(dy)]
    
    if can_reach:
        print("YES")
    else:
        print("NO")