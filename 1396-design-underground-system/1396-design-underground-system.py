class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        self.freqs = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        Name2, t2 = self.ids.pop(id)
        self.pairs[(Name2, stationName)] += t-t2
        self.freqs[(Name2, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pairs[startStation, endStation]/self.freqs[startStation, endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)