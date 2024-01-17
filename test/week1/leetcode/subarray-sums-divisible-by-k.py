class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        res = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        for i in range(len(prefix_sum)):
            res += count[prefix_sum[i] % k]
            count[prefix_sum[i] % k] += 1
        return res

