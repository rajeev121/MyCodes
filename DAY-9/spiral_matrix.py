def spirallyTraverse(self, matrix, r, c):
        total = r * c
        start_row, end_row = 0, r-1
        start_col, end_col = 0, c-1
        spiral_order = []

        while len(spiral_order) < total:
            # traverse right
            spiral_order.extend(matrix[start_row][start_col:end_col+1])
            start_row += 1

            # traverse down
            if len(spiral_order) < total:
                spiral_order.extend([matrix[i][end_col] for i in range(start_row, end_row+1)])
                end_col -= 1

            # traverse left
            if len(spiral_order) < total:
                spiral_order.extend(matrix[end_row][start_col:end_col+1][::-1])
                end_row -= 1

            # traverse up
            if len(spiral_order) < total:
                spiral_order.extend([matrix[i][start_col] for i in range(end_row, start_row-1, -1)])
                start_col += 1

        return spiral_order

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = spirallyTraverse(matrix)
print(result)