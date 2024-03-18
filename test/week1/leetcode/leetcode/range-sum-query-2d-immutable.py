class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                topVal = self.prefix_matrix[i - 1][j] if i > 0 else 0
                leftVal = self.prefix_matrix[i][j - 1] if j > 0 else 0
                duplicateVal = self.prefix_matrix[i - 1][j - 1] if (i > 0 and j > 0) else 0
                self.prefix_matrix[i][j] = self.matrix[i][j] + topVal + leftVal - duplicateVal

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topVal = self.prefix_matrix[row1 - 1][col2] if row1 > 0 else 0
        leftVal = self.prefix_matrix[row2][col1 - 1] if col1 > 0 else 0
        duplicateVal = self.prefix_matrix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        return (self.prefix_matrix[row2][col2] - topVal - leftVal + duplicateVal)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)