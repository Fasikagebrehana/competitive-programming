class MyCalendar:

    def __init__(self):
        # how can I add them as a sorted interval should I use heap or else
        self.cal = []
    def book(self, start: int, end: int) -> bool:
        i = bisect_right(self.cal, (start, end))

        if i > 0 and (max(self.cal[i-1][0], start) < min(self.cal[i-1][1], end)):
            return False
        if i < len(self.cal) and (max(self.cal[i][0], start) < min(self.cal[i][1], end)):
            return False
        self.cal.insert(i, (start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)