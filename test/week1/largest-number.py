class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = [str(num) for num in nums]
        numbers.sort(key = lambda s : s * 100)
        answer = []
        for i in range(len(numbers) - 1, -1, -1):
            answer.append(numbers[i])
        if answer[i] == '0':
            return '0'
        return ''.join(answer)