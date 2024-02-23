class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index_stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1] < temp:
                stack.pop()
                idx = index_stack.pop()
                answer[idx] = i - idx
            stack.append(temp)
            index_stack.append(i)
        return answer