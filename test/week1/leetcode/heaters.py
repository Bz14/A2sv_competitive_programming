class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def check(radius):
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) > radius:
                    j += 1
                else:
                    i += 1
            return i >= len(houses)

        l = 0
        r = max(max(heaters),max(houses))
        ans = max(max(heaters),max(houses))
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans