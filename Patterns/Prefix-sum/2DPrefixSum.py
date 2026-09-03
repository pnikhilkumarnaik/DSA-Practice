def build_prefix_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (
                matrix[i - 1][j - 1]
                + prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
            )

    return prefix


def range_sum(prefix, r1, c1, r2, c2):
    return (
        prefix[r2 + 1][c2 + 1]
        - prefix[r1][c2 + 1]
        - prefix[r2 + 1][c1]
        + prefix[r1][c1]
    )


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

prefix = build_prefix_sum(matrix)

print("Prefix Sum:")
for row in prefix:
    print(row)

print("Rectangle Sum:", range_sum(prefix, 1, 1, 2, 2))

"""
output:
Prefix Sum:
[0, 0, 0, 0, 0]
[0, 1, 3, 6, 10]
[0, 6, 14, 24, 36]
[0, 15, 33, 54, 78]
[0, 28, 60, 96, 136]
Rectangle Sum: 34

"""