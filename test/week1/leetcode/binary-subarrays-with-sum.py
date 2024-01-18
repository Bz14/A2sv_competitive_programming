class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        result  = 0
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        for i in range(len(prefix_sum)):
            result += count[prefix_sum[i] - goal]
            count[prefix_sum[i]] += 1 
        return result