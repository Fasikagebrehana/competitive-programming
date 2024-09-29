class AllOne:

    def __init__(self):
        self.dic = {}
        self.maxx = -inf
        self.minn = inf

    def inc(self, key: str) -> None:
        if key in self.dic:
            self.dic[key] += 1
        else:
            self.dic[key] = 1
        # self.maxx = max(self.maxx, self.dic[key])

    def dec(self, key: str) -> None:
        if key in self.dic:
            if self.dic[key] == 1:
                del self.dic[key]
            else:
                self.dic[key] -= 1
                # self.minn = min(self.min, self.dic[key])

    def getMaxKey(self) -> str:
        return max(self.dic, key=self.dic.get) if self.dic else ""

    def getMinKey(self) -> str:
        return min(self.dic, key=self.dic.get) if self.dic else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()