class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(list)
        self.trip = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        end = stationName
        start, time = self.checkin[id]
        distance = t - time
        if len(self.trip[(start, end)]) == 0 or self.trip is None:
            self.trip[(start, end)] = (distance, 1)
        else:
            x, y = self.trip[(start, end)]
            x += distance
            y += 1
            self.trip[(start, end)] = (x, y)
         


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trip[startStation, endStation]
        return (total / count)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)