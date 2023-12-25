class Bitset:
    def __init__(self, size: int):
        self.bitzero = ['0']* size
        self.bitone = ['1'] * size
        self.counter = 0
        self.size = size
    def fix(self, idx: int) -> None:
        if self.bitzero[idx] == '0':
            self.bitzero[idx] = '1'
            self.bitone[idx] = '0'
            self.counter += 1

    def unfix(self, idx: int) -> None:
        if self.bitzero[idx] == '1':
            self.bitzero[idx] = '0'
            self.bitone[idx] = '1'
            self.counter -= 1

    def flip(self) -> None:
        self.bitzero, self.bitone = self.bitone, self.bitzero
        self.counter = self.size - self.counter
       

    def all(self) -> bool:
        return self.counter == self.size

    def one(self) -> bool:
        return self.counter

    def count(self) -> int:
        return self.counter

    def toString(self) -> str:
        return ''.join(self.bitzero)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()