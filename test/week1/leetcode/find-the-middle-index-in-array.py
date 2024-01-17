class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        for i in range(len(nums)):
            if i == 0 or i == len(nums) - 1:
                if prefix_sum[-1] - nums[i] == 0:
                    return i
            elif prefix_sum[i - 1] == prefix_sum[-1] - prefix_sum[i]:
                return i
        return -1


        