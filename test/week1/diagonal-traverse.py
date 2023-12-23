class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row , col  = 0, 0
        answer = []
        m = len(mat)
        n = len(mat[0])
        isDirection = True

        for i in range(m * n):
            answer.append(mat[row][col])

            if isDirection :
                
                if row == 0 and col != n - 1 :
                    isDirection = False
                    col += 1 
                elif col == n - 1 :
                    isDirection = False
                    row += 1 
                else :
                    row -= 1 
                    col += 1 
            else :
                if col == 0 and row != m - 1 :
                    isDirection = True
                    row += 1 
                elif row == m - 1:
                    isDirection = True
                    col += 1 
                else :
                    col -= 1
                    row += 1 
        return answer