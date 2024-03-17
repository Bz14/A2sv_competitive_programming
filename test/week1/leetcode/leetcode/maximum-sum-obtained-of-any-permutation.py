class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix_sum = [0] * (n  + 1)
        for start, end in requests:
            prefix_sum[start] += 1
            prefix_sum[end + 1] -= 1
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        prefix_sum.sort()
        nums.sort()
        for i in range(n):
            ans += ((prefix_sum[i + 1] * nums[i]) % MOD)
        return ans % MOD
