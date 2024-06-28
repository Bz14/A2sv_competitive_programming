# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(dist):
            start = position[0]
            count = 1
            for i in range(1, n):
                if position[i] - start >= dist:
                    count += 1
                    start = position[i]
                    if count == m:
                        return True
            return False

        l = 1
        r = position[-1] - position[0]
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


        