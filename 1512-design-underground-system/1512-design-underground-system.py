class UndergroundSystem:

    def __init__(self):
        # startstation: time
        self.checkin = defaultdict(list)
        # when checking out we calculate the checkout
        # start,end : time
        self.checkout = defaultdict(list)
        self.count = 0

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # calculate the time that takes from start to end station a
        checkinstation, checkintime = self.checkin[id]
        totalTime = (t - checkintime)
        # self.count += 1
        if not self.checkout[(checkinstation, stationName)]:
            self.checkout[(checkinstation, stationName)] = [totalTime, 1] 

        else:
            self.checkout[(checkinstation, stationName)][0] += totalTime
            self.checkout[(checkinstation, stationName)][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalCount = self.checkout[(startStation, endStation)]
        return totalTime/ totalCount
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)