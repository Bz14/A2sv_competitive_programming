class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_count = Counter(nums)
        result = 0
        for num, count in freq_count.items():
            result += (count * (count - 1)) // 2
        return result