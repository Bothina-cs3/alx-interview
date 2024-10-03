def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # First row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # Start with 1 for the current row
        for j in range(1, i):
            # Calculate the value based on the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End with 1
        triangle.append(row)  # Append the completed row to the triangle

    return triangle
