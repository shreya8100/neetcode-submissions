class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #n = len(matrix)
        #res = [[0 for _ in range(n)] for _ in range(n)]

        #for i in range(n):
            #for j in range(n):
                #res[i][j] = matrix[n - j - 1][i]

        #for i in range(n):
            #for j in range(n):
                #matrix[i][j] = res[i][j]

        left = 0
        right = len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top = left 
                bottom = right

                # save the topleft
                topLeft = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = topLeft
            right -= 1
            left += 1