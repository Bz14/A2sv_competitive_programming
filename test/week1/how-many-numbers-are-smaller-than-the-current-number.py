class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        valDict = defaultdict(list)
        for i, num in enumerate(nums):
            valDict[num].append(i)
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                count = i
            for val in valDict[nums[i]]:
                res[val] = count
        return res
        