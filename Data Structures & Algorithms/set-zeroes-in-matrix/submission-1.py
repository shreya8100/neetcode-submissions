class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        min_row = 0
        max_row = rows - 1
        min_col = 0
        max_col = cols - 1

        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    matrix[i][j] = -1
                    mark_j = j
                    while(mark_j > min_col):
                        if(matrix[i][mark_j - 1] != 0):
                            matrix[i][mark_j-1] = -1
                        mark_j = mark_j - 1

                    mark_j = j
                    while(mark_j < max_col):
                        if(matrix[i][mark_j+1] != 0):
                            matrix[i][mark_j+1] = -1
                        mark_j = mark_j + 1

                    mark_i = i
                    while(mark_i > min_row):
                        if(matrix[mark_i-1][j] != 0):
                            matrix[mark_i-1][j] = -1
                        mark_i = mark_i - 1

                    mark_i = i
                    while(mark_i < max_row):
                        if(matrix[mark_i+1][j] != 0):
                            matrix[mark_i+1][j] = -1
                        mark_i = mark_i + 1
                else:
                    continue
    
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == -1):
                    matrix[i][j] = 0
            