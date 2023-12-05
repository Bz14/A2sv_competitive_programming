class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        refill = capacity
        for i in range(len(plants)):
            if plants[i] > capacity:
                result += 2 * i + 1
                capacity = refill - plants[i]
            else:
                result += 1
                capacity -= plants[i]
        return result
