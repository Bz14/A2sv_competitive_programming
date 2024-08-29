# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = 0
        n = len(arrays)
        for i in range(1, n):
            l, r = arrays[i][0], arrays[i][-1]
            res = max(res, abs(max_val - l), abs(r - min_val))
            min_val = min(min_val, l)
            max_val = max(max_val, r)
        return res 