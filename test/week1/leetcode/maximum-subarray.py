class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        running_sum = 0
        for num in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum += num
            maxSum = max(maxSum, running_sum)
        return maxSum
