class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                value = stack.pop()
                answer[value[1]] = i - value[1]
            stack.append((temp, i))
        return answer