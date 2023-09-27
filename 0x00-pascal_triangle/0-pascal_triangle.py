#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    pascal_triangle
    """
    triangle = []

    for i in range(n):
        if n <= 0:
            return []
        
        triangle.append([1])
        for j in range(1, i + 1):
            if j == i:
                triangle[i].append(1)
            else:
                v = triangle[i-1][j-1] + triangle[i-1][j]
                triangle[i].append(v)

    return triangle
