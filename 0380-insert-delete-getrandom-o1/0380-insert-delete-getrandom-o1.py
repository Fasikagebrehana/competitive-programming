class RandomizedSet:

    def __init__(self):
        
        self.nums = set()
    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        else:
            self.nums.add(val)

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        self.data = list(self.nums)
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()