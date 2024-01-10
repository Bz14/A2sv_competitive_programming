class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        total = 0
        minLen = len(nums) + 1
        while i < len(nums):
            total += nums[i]
            while total >= target:
                minLen = min(minLen, i - j + 1)
                total -= nums[j]
                j += 1
            i += 1
        return minLen % (len(nums) + 1)