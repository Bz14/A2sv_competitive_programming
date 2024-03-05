class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        nums.sort()
        def subsets(idx):
            if path not in ans:
                ans.append(path[:])
        
            for i in range(idx, n):
                path.append(nums[i])
                subsets(i + 1)
                path.pop()

        subsets(0)
        return ans