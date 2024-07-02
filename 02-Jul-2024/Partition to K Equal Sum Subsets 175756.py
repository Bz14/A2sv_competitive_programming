# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k:
            return False
        memo = {}
        n = len(nums)
        nums.sort(reverse=True)
        partition = total_sum//k
        def dp(total, mask):
            if mask == 0:
                return total == 0
            if total == 0:
                return dp(partition , mask)
            if (mask, total) in memo:
                return memo[(mask, total)]
            for i in range(n):
                if mask & (1 << i) and nums[i] <= total:
                    if dp(total - nums[i], mask ^ (1 << i)):
                        memo[(mask, total)] = True
                        return memo[(mask, total)]
            memo[(mask, total)] = False
            return memo[(mask, total)]
        mask = (1 << n) - 1
        return dp(partition, mask)

        