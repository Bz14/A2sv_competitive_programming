class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        maxSum = total
        j = 0
        for i in range(1, len(nums) - k + 1):
            maxSum = max(maxSum, total)
            total = total - nums[j] + nums[k + j]
            j += 1
        maxSum = max(maxSum, total)
        return maxSum / k
            
