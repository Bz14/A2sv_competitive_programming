# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        row_len = len(matrix)
        col_len = len(matrix[0])
        def in_bound(row, col):
            return (0<=row<row_len) and (0<=col<col_len)
        for i in range(row_len):
            for j in range(col_len):
                for x, y in directions:
                    new_row = x + i
                    new_col = y + j
                    if in_bound(new_row, new_col) and matrix[new_row][new_col] > matrix[i][j]:
                        in_degree[(new_row, new_col)] += 1
                        graph[(i,j)].append((new_row, new_col))
        queue = deque([(i,j) for i in range(row_len) for j in range(col_len) if in_degree[(i, j)] == 0])
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for new_row, new_col in graph[(row, col)]:
                    in_degree[(new_row, new_col)] -= 1
                    if in_degree[(new_row, new_col)] == 0:
                        queue.append((new_row, new_col))
            dist += 1
        return dist