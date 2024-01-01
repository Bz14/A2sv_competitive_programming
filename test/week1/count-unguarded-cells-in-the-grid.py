class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['']*n for i in range(m)]
        count = 0
        for i, j in guards:
            matrix[i][j] = "G"
        for i,j in walls:
            matrix[i][j] = "W"
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "G":
                    r = j + 1
                    l = j - 1
                    u = i - 1
                    d = i + 1
                    while r != n and (matrix[i][r] != "W" and matrix[i][r] != "G"):
                        matrix[i][r] = "M"
                        r += 1
                    while l != -1 and (matrix[i][l] != "W" and matrix[i][l] != "G"):
                        matrix[i][l] = "M"
                        l -= 1
                    while u != -1 and (matrix[u][j] != "W" and matrix[u][j] != "G"):
                        matrix[u][j] = "M"
                        u -= 1
                    while d != m and (matrix[d][j] != "W" and matrix[d][j] != "G"):
                        matrix[d][j] = "M"
                        d += 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '':
                    count += 1
        return count