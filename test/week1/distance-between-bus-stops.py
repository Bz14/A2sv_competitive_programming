class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        result = 0
        for i in range(min(start, destination), max(start, destination)):
            result += distance[i]
        result = min(result, sum(distance) - result)
        return result
            