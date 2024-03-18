class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0
        prefix_sum = [nums[0]]
        n = len(nums)
        res_dict = {0 : - 1}
        ans = n
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        rem = prefix_sum[-1] % p
    
        for i in range(len(prefix_sum)):
            value = prefix_sum[i] % p
            r = (value - rem) % p
            if r in res_dict:
                ans = min(ans, i - res_dict[r])
            res_dict[value] = i
        return ans if ans < len(nums) else -1