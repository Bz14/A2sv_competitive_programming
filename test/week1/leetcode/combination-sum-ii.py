class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)
        candidates.sort()
        def combination(idx, target):
            if target == 0:
                ans.append(path[:])
            if target < 0:
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i],)
                combination(i + 1, target - candidates[i])
                path.pop()

        combination(0, target)
        return ans