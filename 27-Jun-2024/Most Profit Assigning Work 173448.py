# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = []
        for d,p in zip(difficulty, profit):
            arr.append((d, p))
        arr.sort()
        worker.sort()
        l = 0
        r = 0
        res = 0
        temp = 0
        while l < len(arr) and r < len(worker):
            while l < len(arr) and worker[r] >= arr[l][0]:
                temp = max(temp, arr[l][1])
                l += 1
            res += temp
            r += 1
        res += (len(worker) - r) * temp if r < len(worker) else 0
        return res