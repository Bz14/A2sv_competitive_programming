# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row_len = len(grid2)
        col_len = len(grid2[0])
        visited = set()
        ans = 0
        is_sub_island = True

        def in_bound(row, col):
            return 0<=row<row_len and 0<=col<col_len

        def DFS(row, col):
            nonlocal is_sub_island
            if grid1[row][col] != 1:
                is_sub_island = False
            visited.add((row, col))
            for x,y in directions:
                new_row = x + row
                new_col = y + col
                if in_bound(new_row, new_col) and (new_row, new_col) not in visited and grid2[new_row][new_col] != 0:
                    DFS(new_row, new_col)
    
        for i in range(row_len):
            for j in range(col_len):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    DFS(i, j)
                    if is_sub_island:
                        ans += 1
                    is_sub_island = True
        return ans


        