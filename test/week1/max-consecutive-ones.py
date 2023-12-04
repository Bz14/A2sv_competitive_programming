class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        idx = 0
        maxOnes = 0
        for i , num in enumerate(nums):
            if num != 1:
                maxOnes = max(maxOnes, i - idx)
                idx = i + 1
        maxOnes = max(maxOnes, len(nums) - idx)
        return maxOnes