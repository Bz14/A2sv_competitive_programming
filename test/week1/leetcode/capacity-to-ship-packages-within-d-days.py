class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            count = 0
            total = 0
            if capacity < max(weights):
                return False
            for val in weights:
                total += val
                if total == capacity:
                    count += 1
                    total = 0
                elif total > capacity:
                    count += 1
                    total = val
            if total > 0:
                count += 1
            
            return count <= days
        l = 0
        r = sum(weights)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
            print(mid)
        return ans

