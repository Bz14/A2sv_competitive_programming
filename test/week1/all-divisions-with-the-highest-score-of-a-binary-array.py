class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        oneCount = sum(nums)
        zeroCount = 0
        res = {}
        res[0] = oneCount
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                oneCount -= 1
            res[i + 1] = zeroCount + oneCount
        maxValue = max(res.values())
        return [key for key, value in res.items() if value == maxValue]
            
        
        
        """count = {}
        for i in range(len(nums)):
            if i != 0:
                count[i] = Counter(nums[0:i])[0] + Counter(nums[i:len(nums)])[1]
        res = Counter(nums)
        count[len(nums)] = res[0]
        count[0] = res[1]
        value = max(count.values())
        return [k for k, v in count.items() if v == value]"""
                
            
