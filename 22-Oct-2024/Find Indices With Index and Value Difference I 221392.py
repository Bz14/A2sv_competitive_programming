# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]

        for i in range(n):
            r = i + indexDifference
            while r < n:
                if abs(nums[i] - nums[r]) >= valueDifference:
                    return [i, r]
                r += 1
        return ans
