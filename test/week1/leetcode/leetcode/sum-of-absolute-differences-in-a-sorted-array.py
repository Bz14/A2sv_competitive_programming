class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        ans = []
        for i in range(n):
            if i == 0:
                right_value = prefix_sum[-1] - (nums[i] * (n - i))
                value = right_value
            elif i == n - 1:
                left_value = (nums[i] * i) - prefix_sum[i - 1]
                value = left_value
            else:
                right_value = prefix_sum[-1] - prefix_sum[i - 1] - (nums[i] * (n - i))
                left_value = (nums[i] * i) - prefix_sum[i - 1]
                value = right_value + left_value
            ans.append(value)
        return ans