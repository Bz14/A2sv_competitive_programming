class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        res = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                diagonal[i + j].append(mat[i][j])
        for key in diagonal:
            if key % 2 != 0:
                for i in range(len(diagonal[key])):
                    res.append(diagonal[key][i])
            else:
                for i in range(len(diagonal[key]) - 1, -1, -1):
                    res.append(diagonal[key][i])
        return res