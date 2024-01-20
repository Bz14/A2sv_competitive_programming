class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = defaultdict(list)
        ans = []
        for x, y in points:
            res[(x ** 2) + (y ** 2)].append([x, y])
        sorted_arr = sorted(res)
        for key in sorted_arr:
            for value in res[key]:
                if len(ans) > k - 1:
                    break
                ans.append(value)
        return ans