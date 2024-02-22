class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {num:i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                value = stack.pop()
                res[count[value]] = num
            if num in count:
                stack.append(num)
        return res
