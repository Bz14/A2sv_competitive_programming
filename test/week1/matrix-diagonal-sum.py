class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    total += mat[i][j]
        i = 0
        j = len(mat) - 1
        for _ in range(len(mat)):
            if i != j:
                total += mat[i][j]
            i += 1
            j -= 1
        return total



