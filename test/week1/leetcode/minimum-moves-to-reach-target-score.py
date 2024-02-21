class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                target //= 2
                res += 1
            else:
                target -= 1
                res += 1
        if target > 1:
            res += target - 1
        return res

