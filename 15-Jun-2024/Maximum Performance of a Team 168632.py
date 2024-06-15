# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = []
        for e, s in zip(efficiency, speed):
            arr.append((e, s))
        arr.sort(reverse = True)
        heap = []
        ans = 0
        res = 0
        for efficiency, speed in arr:
            if len(heap) == k:
                res -= heappop(heap)
            res += speed
            heappush(heap, speed)
            ans = max(ans, res * efficiency)
        return ans % (10**9 + 7)