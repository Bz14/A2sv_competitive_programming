class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        res = sum
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            res = max(res,sum)
        return res/k