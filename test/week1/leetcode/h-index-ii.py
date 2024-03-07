class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(amount):
            count = 0
            for cite in citations:
                if cite >= amount:
                    count += 1
            return count >= amount
        l = 0
        r = max(citations)
        maxVal = 0

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                maxVal = max(maxVal, mid)
                l = mid + 1
            else:
                r = mid - 1
        return maxVal
