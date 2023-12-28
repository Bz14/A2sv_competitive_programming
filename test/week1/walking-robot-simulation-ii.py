class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.position= [0, 0]
        self.direction = "East"

    def step(self, num: int) -> None:
        i = 0
        num = num % ((self.height + self.width - 2)  * 2)
        if num != 0:
            while i < num:
                if self.direction == "East":
                    if self.position[0] != self.width - 1:
                        self.position[0] += 1
                    else:
                        self.direction = "North"
                        num += 1
                elif self.direction == "North":
                    if self.position[1] != self.height - 1:
                        self.position[1] += 1
                    else:
                        self.direction = "West"
                        num  += 1
                elif self.direction == "West":
                    if self.position[0] != 0:
                        self.position[0] -= 1
                    else:
                        self.direction = "South"
                        num += 1
                elif self.direction == "South":
                    if self.position[1] != 0:
                        self.position[1] -= 1
                    else:
                        self.direction = "East"
                        num += 1
                i += 1
        elif self.position == [0, 0] and self.direction == "East":
            self.direction = "South"


    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
