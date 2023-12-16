from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.freqTracker = []
        self.freq = defaultdict(int)
        self.nums = {}
    def add(self, number: int) -> None:
        if number in self.nums:
            self.freq[self.nums[number]] -= 1
            self.nums[number] += 1
        else:
            self.nums[number] = 1
        self.freq[self.nums[number]] += 1
    def deleteOne(self, number: int) -> None:
        if number in self.nums:
            if self.nums[number] > 1:
                self.freq[self.nums[number]] -= 1
                self.nums[number] -= 1
                self.freq[self.nums[number]] += 1
            elif self.nums[number] == 1:
                del self.nums[number] 
                self.freq[1] -= 1
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq and self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)