class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        min_val = min(heights)
        max_val = max(heights)
        res = [0] * (max_val - min_val  + 1)
        for i in range(len(heights)):
            res[heights[i] - min_val] += 1
        ans = []
        for i in range(len(res)-1, -1, -1):
            for j in range(res[i]):
                if res[i] != 0:
                    idx = heights.index(i + min_val)
                    ans.append(names[idx])
        return ans