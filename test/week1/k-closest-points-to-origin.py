class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = defaultdict(list)
        ans = []
        for x, y in points:
            res[(x ** 2) + (y ** 2)].append([x, y])
        sorted_dict = dict(sorted(res.items()))
        for key, values in sorted_dict.items():
            for value in values:
                if k == 0:
                    break
                ans.append(value)
                k -= 1
        return ans