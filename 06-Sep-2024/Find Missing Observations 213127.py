# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        length = len(rolls) + n
        missing_sum = (mean * length) - sum(rolls)
        if missing_sum < 0:
            return []
        res = missing_sum // n
        rem = missing_sum % n
        if res > 6 or (res == 6 and rem != 0):
            return []
        ans = [res for _ in range(n)]
        i = 0
        if res == 0:
            return []
        while rem > 0:
            add = 6 - ans[i]
            if add > rem:
                ans[i] += rem
            else:
                ans[i] += add
            rem -= add
            i += 1
        return ans
        