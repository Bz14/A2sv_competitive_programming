# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        minVal = nums[-1] - nums[3]
        minVal = min(minVal, nums[-2] - nums[2])
        minVal = min(minVal, nums[-3] - nums[1])
        minVal = min(minVal, nums[-4] - nums[0])
        return minVal