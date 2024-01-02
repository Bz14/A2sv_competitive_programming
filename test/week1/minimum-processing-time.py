class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        maxTime = 0
        i = 0
        for time in processorTime:
            maxTime = max(maxTime, time + max(tasks[i : i + 4]))
            i += 4
        return maxTime