# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.size = maxSize
        
    def push(self, x: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        val = self.arr.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        length = k
        if len(self.arr) < k:
            length = len(self.arr)
        for i in range(length):
            self.arr[i] += val
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)