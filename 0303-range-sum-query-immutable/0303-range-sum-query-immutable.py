class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        self.temp = [0] * len(self.nums)
        while left <= right:
            self.temp[left] += self.nums[left]
            left += 1
        return sum(self.temp)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)