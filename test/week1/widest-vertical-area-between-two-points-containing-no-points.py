class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = [x for x, y in points]
        width.sort()
        res = 0
        for i in range(len(width) - 1):
            res = max(res, width[i + 1] - width[i])
        return res
