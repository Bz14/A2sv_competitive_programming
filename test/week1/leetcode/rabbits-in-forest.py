class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for key, value in count.items():
            numberOfPairs = ceil(value / (key + 1))
            res += numberOfPairs * (key + 1)
        return res