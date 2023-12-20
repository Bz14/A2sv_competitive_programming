class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.randomArr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.index[val] = len(self.randomArr)
            self.randomArr.append(val)
            return True
        
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.index:
        
            self.index[self.randomArr[-1]] = self.index[val]
            self.randomArr[self.index[val]] = self.randomArr[-1]

            self.randomArr.pop()
            self.index.pop(val)
            
            return True
        
        return False

    def getRandom(self) -> int:

        num = random.randint(0, len(self.randomArr) - 1)
        return self.randomArr[num]