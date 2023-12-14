class OrderedStream:

    def __init__(self, n: int):
        self.lis = [None] * n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lis[idKey - 1] = value
        ans = []
        while self.p < len(self.lis) and self.lis[self.p] is not None:
            ans.append(self.lis[self.p])
            self.p += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)