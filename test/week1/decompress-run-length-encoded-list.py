class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                for j in range(nums[i]):
                    res.append(nums[i + 1])
        return res