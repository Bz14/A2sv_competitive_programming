class TimeMap:

    def __init__(self):
        self.keyValueStore = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValueStore[key].append([timestamp, value])

        
    def get(self, key: str, timestamp: int) -> str:
        values = self.keyValueStore[key]
        ans = [0,""]
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                ans = ans if ans[0] > values[mid][0] else values[mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans[1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)