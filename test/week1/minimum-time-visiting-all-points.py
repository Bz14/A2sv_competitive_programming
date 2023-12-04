class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            val1 = points[i]
            val2 = points[i + 1]
            res += max(abs(val2[0] - val1[0]), abs(val2[1] - val1[1]))
        return res
