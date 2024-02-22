class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if not self.queue1:
            self.queue1.append(x)
        else:
            while self.queue1:
                self.queue2.append(self.queue1.pop())
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.pop())
    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()