class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)
        def combination(idx, target):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return
            for i in range(idx, n):
                path.append(candidates[i])
                combination(i, target - candidates[i])
                path.pop()
        combination(0, target)
        return ans