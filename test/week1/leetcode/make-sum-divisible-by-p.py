class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = [nums[0]]
        res_dict = {0:-1}
        ans = len(nums)
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        rem = prefix_sum[-1] % p
        if rem == 0:
            return 0
        for i in range(len(prefix_sum)):
            value = prefix_sum[i] % p
            r = (value - rem) % p
            if r in res_dict:
                j = res_dict[r]
                ans = min(ans, i - j)
            res_dict[value] = i
        return ans if ans < len(nums) else -1

