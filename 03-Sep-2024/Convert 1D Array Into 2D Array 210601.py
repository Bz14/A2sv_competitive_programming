# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        if length / m != n:
            return []
        ans = []
        start = 0
        gap = length // m if length > m else n
        for i in range(m):
            ans.append(original[start:start + gap])
            start += gap
        return ans