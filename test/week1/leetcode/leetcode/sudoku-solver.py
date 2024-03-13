class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """    
        def isValid(r, c, k):
            for i in range(9):             
                if (board[i][c] == k or 
                    board[r][i] == k or 
                    board[ 3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k):
                    return False
            return True    
        def sudokuSolver(r, c): 
            if r == 9:
                return True
            if c == 9:
                return sudokuSolver(r + 1, 0)   
            if board[r][c] == '.':
                for i in range(1, 10):
                    if isValid(r, c, str(i)):
                        board[r][c] = str(i)
                        if sudokuSolver(r, c + 1):
                            return True
                        board[r][c] = '.'
                return False
            return sudokuSolver(r, c + 1)        

        sudokuSolver(0,0)

        

       
