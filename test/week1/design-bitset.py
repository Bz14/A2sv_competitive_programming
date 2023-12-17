class Bitset:

    def __init__(self, size: int):
        self.bitArray = [0 for i in range(size)]
        self.flipArray = [1 for i in range(size)]
        self.zeroCount = size
        self.oneCount = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.bitArray[idx]:
            self.oneCount += 1
            self.zeroCount -= 1
        self.bitArray[idx] = 1
        self.flipArray[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.bitArray[idx]:
            self.oneCount -= 1
            self.zeroCount += 1
        self.bitArray[idx] = 0
        self.flipArray[idx] = 1

    def flip(self) -> None:
        self.zeroCount , self.oneCount = self.oneCount, self.zeroCount
        self.bitArray, self.flipArray = self.flipArray, self.bitArray

    def all(self) -> bool:
        return self.oneCount == self.size

    def one(self) -> bool:
        return self.oneCount > 0

    def count(self) -> int:
        return self.oneCount

    def toString(self) -> str:
        res =''
        for i in self.bitArray:
            res += str(i)
        return res
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()