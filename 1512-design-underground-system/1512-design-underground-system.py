class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.total = {} # (startstation, endstation) : [totaltime, count]


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s, time = self.checkin[id]
        trip = (s, stationName)
        if trip not in self.total:
            self.total[trip] = [0, 0]
        self.total[trip][0] += t - time
        self.total[trip][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start, end = self.total[(startStation, endStation)]
        average = start / end
        return average


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)