# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        ans = 0
        for _ in range(k):
            ans += maxVal
            maxVal += 1
        return ans