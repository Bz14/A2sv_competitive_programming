class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        lookup = set()
        j = 0
        maxVal = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] not in lookup:
                total += nums[i]
                lookup.add(nums[i])
            else:
                maxVal = max(maxVal, total)
                while nums[i] in lookup:
                    lookup.remove(nums[j])
                    total -= nums[j]
                    j += 1
                lookup.add(nums[i])
                total += nums[i]
        maxVal = max(maxVal, total)
        return maxVal

