class Solution:
    def equalPairs(self, grid):
        n = len(grid)

        # Store rows as tuples with their frequency
        row_count = {}

        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        count = 0

        # Compare each column with stored rows
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))

            if col in row_count:
                count += row_count[col]

        return count