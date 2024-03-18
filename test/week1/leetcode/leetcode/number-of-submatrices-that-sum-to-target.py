class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])
        prefix_matrix = [[0] * col_len for _ in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                top_val = prefix_matrix[i - 1][j] if i > 0 else 0
                left_val = prefix_matrix[i][j - 1] if j > 0 else 0
                duplicate_val = prefix_matrix[i - 1][j - 1] if (i > 0 and j > 0) else 0
                prefix_matrix[i][j] = matrix[i][j] + top_val + left_val - duplicate_val
        ans = 0
        for start_row in range(row_len):
            for end_row in range(start_row, row_len):
                count = defaultdict(int)
                count[0] = 1
                for col in range(col_len):
                    duplicate_val = prefix_matrix[start_row - 1][col] if start_row > 0 else 0
                    current_value = prefix_matrix[end_row][col] - duplicate_val
                    ans += count[current_value - target]
                    count[current_value] += 1
        return ans