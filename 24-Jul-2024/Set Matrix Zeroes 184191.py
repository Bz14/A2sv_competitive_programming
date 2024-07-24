# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row = 0 in matrix[0]
        col = 0 in [matrix[i][0] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if row:
            matrix[0] = [0] * m
        if col:
            for i in range(n):
                matrix[i][0] = 0
