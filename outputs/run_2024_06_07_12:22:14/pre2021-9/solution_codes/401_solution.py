n = int(input())
planks = list(map(int, input().split()))

has_square = False
has_rect = False

for plank in planks:
    if planks.count(plank) >= 4 and not has_square:
        has_square = True
    if planks.count(plank) >= 2 and 'rect_sides' in locals() and (rect_sides != plank or has_rect):
        has_rect = True
    if planks.count(plank) >= 2 and 'rect_sides' not in locals():
        rect_sides = plank

q = int(input())

for _ in range(q):
    event = input().split()
    if event[0] == '+':
        planks.append(int(event[1]))
    else:
        planks.remove(int(event[1]))
    
    has_square = False
    has_rect = False
    
    for plank in planks:
        if planks.count(plank) >= 4 and not has_square:
            has_square = True
        if planks.count(plank) >= 2 and 'rect_sides' in locals() and (rect_sides != plank or has_rect):
            has_rect = True
        if planks.count(plank) >= 2 and 'rect_sides' not in locals():
            rect_sides = plank
    
    if has_square and has_rect:
        print("YES")
    else:
        print("NO")