# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        n = len(nums)
        i = 0
        count = 0
        ans = 1
        bit = nums[0]
        while i < n:
            if i > 0 and nums[i] != nums[i - 1]:
                count = 1
                bit = nums[i]
            else:
                bit &= nums[i]
                count += 1
            i += 1
            if bit >= max_val:
                ans = max(ans, count)
        return ans


