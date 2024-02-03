class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        length = len(set(nums))
        count_dict = defaultdict(int)
        l = 0
        res = 0
        totalSubarray = (len(nums) * (len(nums) + 1)) // 2
        for r in range(len(nums)):
            count_dict[nums[r]] += 1
            while len(count_dict) == length:
                count_dict[nums[l]] -= 1
                if count_dict[nums[l]] == 0:
                    del count_dict[nums[l]]
                l += 1
            res += r - l + 1
        return totalSubarray - res