# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maxVal = max(nums)
        minVal = min(nums)
        size = max(1, (maxVal - minVal) // len(nums) - 1)
        bucket = [[None, None] for _ in range((maxVal - minVal) // size + 1)]
        minVal = min(nums)
        for num in nums:
            idx = (num - minVal) // size
            if bucket[idx][0] is None:
                bucket[idx][0] = bucket[idx][1] = num
            else:
                bucket[idx][0] = min(bucket[idx][0], num)
                bucket[idx][1] = max(bucket[idx][1], num)
        max_gap = 0
        prev_max = bucket[0][1]
        
        for i in range(1, (maxVal - minVal) // size + 1):
            if bucket[i][0] is None:
                continue
            max_gap = max(max_gap, bucket[i][0] - prev_max)
            prev_max = bucket[i][1]
        
        return max_gap