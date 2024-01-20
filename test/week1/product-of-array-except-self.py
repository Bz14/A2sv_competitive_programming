class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pre = 1
        for i in range(len(nums)):
           result[i] = pre
           pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1 , -1):
            result[i]*= post
            post *= nums[i]
        return result