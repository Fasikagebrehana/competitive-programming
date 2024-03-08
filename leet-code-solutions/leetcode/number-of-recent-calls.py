class RecentCounter:

    def __init__(self):
        self.request = deque()

    def ping(self, t: int) -> int:
        self.request.append(t)
        diff = t - 3000
        while self.request[0] < diff:
            self.request.popleft()
        return len(self.request)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)