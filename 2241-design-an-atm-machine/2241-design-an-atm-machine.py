class ATM:

    def __init__(self):
        self.counter = {20 : 0, 50 : 0, 100 : 0, 200 : 0, 500 : 0}

    def deposit(self, banknotesCount: List[int]) -> None:
        self.counter[20] += banknotesCount[0]
        self.counter[50] += banknotesCount[1]
        self.counter[100] += banknotesCount[2]
        self.counter[200] += banknotesCount[3]
        self.counter[500] += banknotesCount[4]
        

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        values = list(self.counter.values())
        
        five = amount // 500         
        if self.counter[500] >= five:
            self.counter[500] -= five
        else:
            five = self.counter[500]
            self.counter[500] = 0
        ans[4] += five
        amount = amount - (five * 500)

        two = amount // 200         
        if self.counter[200] >= two:
            self.counter[200] -= two
        else:
            two = self.counter[200]
            self.counter[200] = 0
        ans[3] += two
        amount = amount - (two * 200)

        one = amount // 100         
        if self.counter[100] >= one:
            self.counter[100] -= one
        else:
            one = self.counter[100]
            self.counter[100] = 0
        ans[2] += one
        amount = amount - (one * 100)

        fifty = amount // 50        
        if self.counter[50] >= fifty:
            self.counter[50] -= fifty
        else:
            fifty = self.counter[50]
            self.counter[50] = 0
        ans[1] += fifty
        amount = amount - (fifty * 50)

        twenty = amount // 20        
        if self.counter[20] >= twenty:
            self.counter[20] -= twenty
        else:
            twenty = self.counter[20]
            self.counter[20] = 0
        ans[0] += twenty
        amount = amount - (twenty * 20)

        if amount == 0:
            return ans

        self.counter[20] = values[0]
        self.counter[50] = values[1]
        self.counter[100] = values[2]
        self.counter[200] = values[3]
        self.counter[500] = values[4]
        return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)