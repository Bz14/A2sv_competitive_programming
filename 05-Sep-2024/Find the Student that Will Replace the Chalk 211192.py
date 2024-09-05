# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        res = k // total
        k -= (res * total)
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c