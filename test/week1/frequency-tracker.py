class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.nums[number]] -= 1
        self.nums[number] += 1
        self.freq[self.nums[number]] += 1
    
    def deleteOne(self, number: int) -> None:
        if self.freq[self.nums[number]] > 0:
            self.freq[self.nums[number]] -= 1
            self.nums[number] -= 1
            self.freq[self.nums[number]] += 1


    def hasFrequency(self, frequency: int) -> bool: 
        if frequency in self.freq and self.freq[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)