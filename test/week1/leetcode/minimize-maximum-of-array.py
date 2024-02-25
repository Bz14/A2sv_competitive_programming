class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, ceil(total / (i + 1)))
        return res