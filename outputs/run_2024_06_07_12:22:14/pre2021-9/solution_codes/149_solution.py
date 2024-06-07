for _ in range(int(input())):
    a1, a2, a3, a4 = sorted(map(int, input().split()), reverse=True)
    # Forming the rectangle using the given segments
    area = a1 * a3
    print(area)