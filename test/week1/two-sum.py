class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumdict = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in sumdict:
                return [idx, sumdict[diff]]
            sumdict[num] = idx