class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        transposeArr= [[0] * row for _ in range(column)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposeArr[j][i] = matrix[i][j]
        return transposeArr