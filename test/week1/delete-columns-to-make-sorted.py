class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleteCount = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    deleteCount += 1
                    break
        return deleteCount
        """
        ["rrjk","furt","guzm"]"""