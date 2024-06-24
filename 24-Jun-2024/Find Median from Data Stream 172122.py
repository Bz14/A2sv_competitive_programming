# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -(num))
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)

        if len(self.max_heap) - 1 > len(self.min_heap):
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
    
        if len(self.min_heap) - 1 > len(self.max_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
        if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()