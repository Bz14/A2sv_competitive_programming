# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = 0
        ans = []
        n = len(nums)
        bit = (1 << maximumBit) - 1
        for i in range(n):
            prefix_xor ^= nums[i]
        j = n - 1
        for i in range(n):
            ans.append(prefix_xor ^ bit)
            prefix_xor ^= nums[j]
            j -= 1
        return ans

