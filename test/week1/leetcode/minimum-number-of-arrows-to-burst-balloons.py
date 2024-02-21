class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(1, len(points)):
            end = min(end, points[i][1])
            if not (points[i][0] >= start and points[i][0] <= end):
                arrows += 1
                end = points[i][1]
            start = points[i][0]
        return arrows
