for _ in range(int(input())):
    input()  # Ignore blank line
    n = int(input())
    dishes = []
    for _ in range(n):
        a, b, m = map(int, input().split())
        dishes.append((a, b, m))

    min_variety = min([min(dish[:2]) for dish in dishes])
    print(min_variety)
    
    for dish in dishes:
        x = min(dish[0], min_variety)
        y = max(0, dish[2] - x)
        print(x, y)