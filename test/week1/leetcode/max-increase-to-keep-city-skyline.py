class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        n = len(grid)
        res = 0
        for row in grid:
            rowMax.append(max(row))
        for i in range(n):
            check = []
            for j in range(n):
                check.append(grid[j][i])
            colMax.append(max(check))
        for i in range(n):
            for j in range(n):
                res += abs(grid[i][j] - min(rowMax[i], colMax[j]))
        return res