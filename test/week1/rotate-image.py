class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        l = 0
        r = len(matrix) - 1
        for i in range(len(matrix) // 2):
            for j in range(len(matrix)):
                matrix[j][l], matrix[j][r] = matrix[j][r], matrix[j][l]
            l += 1
            r -= 1
        