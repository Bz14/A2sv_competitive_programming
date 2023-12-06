class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        j = int(len(nums)/3)
        i = 0
        nums.sort()
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                result.add(nums[i])
            i += 1
            j += 1  
        return list(result)
        
        """return list(set([num for num in nums if nums.count(num) > len(nums) / 3]))"""