class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

        
        """
        1 2 3 4
        5 1 2 3
        9 5 1 2

        13 24

        1 1 1 -> 00 11 22
        2 2 2 -> 01 12 23
        3 3 -> 02 13
        4 -> 03
        """