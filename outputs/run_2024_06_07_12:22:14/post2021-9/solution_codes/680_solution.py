for _ in range(int(input())):
    input()  # Read blank line
    n, m = map(int, input().split())
    dishes = [list(map(int, input().split())) for _ in range(n)]
    
    total_fish = sum(d[0] for d in dishes)
    total_meat = sum(d[1] for d in dishes)
    
    balance = abs(total_fish - total_meat)
    
    print(balance)
    for dish in dishes:
        x = min(dish[0], m)
        y = m - x
        print(x, y)