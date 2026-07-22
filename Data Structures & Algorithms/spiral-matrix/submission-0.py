class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        m = len(matrix)
        n = len(matrix[0])

        result = [0] * (m * n)

        min_row, max_row = 0, m - 1
        min_col, max_col = 0, n - 1

        while count < m * n:
            for i in range(min_col, max_col + 1):
                result[count] = matrix[min_row][i]
                count += 1
            min_row += 1

            for i in range(min_row, max_row + 1):
                result[count] = matrix[i][max_col]
                count += 1
            max_col -= 1

            if min_row <= max_row:
                for i in range(max_col, min_col - 1, -1):
                    result[count] = matrix[max_row][i]
                    count += 1
                max_row -= 1

            if min_col <= max_col:
                for i in range(max_row, min_row - 1, -1):
                    result[count] = matrix[i][min_col]
                    count += 1
                min_col += 1

        return result