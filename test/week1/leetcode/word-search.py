class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        path = set()
        row = len(board)
        col = len(board[0])
        def findWord(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= row or j >= col or (i, j) in path or word[idx] != board[i][j]:
                return False
            path.add((i, j))
            l = findWord(i, j + 1, idx + 1)
            r = findWord(i, j - 1, idx + 1)
            u = findWord(i + 1, j, idx + 1)
            d = findWord(i - 1, j, idx + 1)
            path.remove((i, j))
            return l or r or u or d

        for i in range(row):
             for j in range(col):
                if findWord(i, j, 0):
                    return True
        return False