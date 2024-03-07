class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startValue = [start for start, end in intervals]
        n = len(startValue)
        lookup = {intervals[i][0] : i for i in range(n)}
        startValue.sort()
        ans = [-1]*(n) 
        i = 0
        for start,end in intervals:
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                if startValue[mid] >= end:
                    ans[i] = lookup[startValue[mid]]
                    r = mid - 1
                else:
                    l = mid + 1
            i += 1
        return ans
