class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        res = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                res[i][j] = matrix[n - j - 1][i]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]