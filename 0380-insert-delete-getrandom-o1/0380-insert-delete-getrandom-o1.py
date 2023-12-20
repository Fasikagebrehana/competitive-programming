import random
class RandomizedSet:

    def __init__(self):
        self.randset = []
        self.rset = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.rset:
            self.randset.append(val)
            self.rset[val] = len(self.randset) - 1
            return True
        return False
                
    def remove(self, val: int) -> bool:
        if val in self.rset:
            index_to_remove = self.rset[val]
            last_element = self.randset[-1]
            self.randset[index_to_remove], self.randset[-1] = self.randset[-1], self.randset[index_to_remove]
            self.rset[last_element] = index_to_remove
            self.randset.pop()
            del self.rset[val]
            return True
        return False
    def getRandom(self) -> int:
        if len(self.randset) > 0:
            return random.choice(self.randset)
        return None


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()