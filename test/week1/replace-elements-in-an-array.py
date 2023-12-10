class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        new_dict = defaultdict()

        for i, num in enumerate(nums):
            new_dict[num] = i
        for a,b in operations:
            nums[new_dict[a]] = b
            new_dict[b] = new_dict[a]
        return nums

