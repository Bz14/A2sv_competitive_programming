class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        count = 0
        minVal = min(nums)
        for i in range(1, len(nums)):
            if nums[i] != minVal:
                count += 1
                res += count
                minVal = nums[i]
            else:
                res += count
        return res