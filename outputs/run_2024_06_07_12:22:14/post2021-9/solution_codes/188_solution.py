import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def point_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    b1 = ((x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)) < 0.0
    b2 = ((x - x2) * (y3 - y2) - (y - y2) * (x3 - x2)) < 0.0
    b3 = ((x - x3) * (y1 - y3) - (y - y3) * (x1 - x3)) < 0.0

    return b1 == b2 and b2 == b3

t = int(input().strip())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Calculate distances between vertices
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    # Check if any of the vertices are inside the triangle
    unsafe_length = 0
    if not point_inside_triangle(x1, y1, x2, y2, x3, y3, x1, 0):
        unsafe_length += a
    if not point_inside_triangle(x1, y1, x2, y2, x3, y3, x2, 0):
        unsafe_length += b
    if not point_inside_triangle(x1, y1, x2, y2, x3, y3, x3, 0):
        unsafe_length += c

    print("{:.9f}".format(unsafe_length))