class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] > nums2[j]:
                    nums2[i], nums2[j] = nums2[j], nums2[i]
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res