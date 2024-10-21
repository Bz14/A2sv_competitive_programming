# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        ans = 0

        for _ in range(k):
            val = abs(heappop(heap))
            ans += val
            heappush(heap, -ceil(val/3))

        return ans

            
