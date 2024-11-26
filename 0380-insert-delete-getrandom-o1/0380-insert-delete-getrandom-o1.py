class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.nums.append(val)
            self.dic[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            # temp = self.dic[self.nums[-1]]
            idx = self.dic[val]
            num = self.nums[-1]
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.dic[num] = idx
            self.dic[val] = len(self.nums) - 1
            self.nums.pop()
            del self.dic[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()