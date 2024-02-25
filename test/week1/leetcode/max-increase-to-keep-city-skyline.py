class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        n = len(grid)
        res = 0
        for i in range(n):
            maxCol = grid[0][i]
            for j in range(n):
                maxCol = max(maxCol, grid[j][i])
            colMax.append(maxCol)
            rowMax.append(max(grid[i]))
        for i in range(n):
            for j in range(n):
                res += abs(grid[i][j] - min(rowMax[i], colMax[j]))
        return res