#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows of the triangle.
    
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Create a new row filled with zeros
        row = [0] * (i + 1)
        # Set the first and last element of each row to 1
        row[0], row[-1] = 1, 1
        
        # Each triangle element (except for the first and last) is the sum of the two above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle
