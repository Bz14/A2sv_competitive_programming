class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in numdict:
                return [idx, numdict[diff]]
            numdict[num] = idx