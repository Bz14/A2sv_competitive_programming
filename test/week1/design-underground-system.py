class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(tuple)
        self.stations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
       self.checkin[id] = tuple([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkin[id][0]
        time = self.checkin[id][1]
        self.stations[tuple([startStation, stationName])].append(t - time)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stations[tuple([startStation, endStation])]) / len(self.stations[tuple([startStation, endStation])])
       


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)