class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(amount):
            count = 0
            for pile in piles:
                if pile < amount:
                    count += 1
                else:
                    count += (pile // amount) + (1 if pile % amount != 0 else 0)
            return count <= h
        if sum(piles) <= h:
            return 1
        l = 1
        r = max(piles)
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans