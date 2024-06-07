for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    other_row = ""
    for char in s:
        if char == "L":
            other_row += "R"
        elif char == "R":
            other_row += "L"
        elif char == "U":
            other_row += "D"
        elif char == "D":
            other_row += "U"
    
    print(other_row)