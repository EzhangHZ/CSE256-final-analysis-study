t = int(input())  # Read the number of regular polygons available in the market

for i in range(t):
    n = int(input())  # Read the number of sides of the current regular polygon
    if n % 4 == 0:
        print("YES")  # If n is multiple of 4, the regular polygon is beautiful
    else:
        print("NO")  # Otherwise, the regular polygon is not beautiful