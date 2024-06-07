# Solution Code:

for _ in range(int(input())):
    n = int(input())
    level = input().strip()
    
    moves = 0  # Initialize move count
    
    prev_sheep_idx = -1  # Initialize previous sheep index
    
    for i, char in enumerate(level):
        if char == '*':  # Find the current sheep position
            if prev_sheep_idx == -1:  # For the first sheep
                prev_sheep_idx = i
            else:
                moves += i - prev_sheep_idx - 1  # Calculate the moves needed to line up sheep
                prev_sheep_idx += 1  # Update previous sheep index
    
    print(moves)