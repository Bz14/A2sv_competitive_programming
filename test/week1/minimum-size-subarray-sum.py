class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        total = 0
        minLen = len(nums) + 1
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minLen = min(minLen, i - j + 1)
                total -= nums[j]
                j += 1
        return minLen % (len(nums) + 1)