class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.newMatrix = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(self.matrix)):
            self.newMatrix[i][0] = self.matrix[i][0]
            for j in range(1, len(self.matrix[0])):
                self.newMatrix[i][j] = self.newMatrix[i][j - 1] + self.matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += (self.newMatrix[i][col2] - (self.newMatrix[i][col1-1] if col1 != 0 else 0))
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 3 0 1 4 2
# 3 3 4 5 7