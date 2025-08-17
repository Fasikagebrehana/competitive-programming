class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        positive = []
        negative = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        anspositive = 0
        ansnegative = 0
        for i in range(32):
            countpositive = 0
            countnegative = 0


            for num in positive:
                countpositive += bool(num & (1 << i))

            if countpositive % 3 != 0:
                anspositive = anspositive | (1 << i)

            for num in negative:
                countnegative += bool(abs(num) & (1 << i))
            
            if countnegative % 3 != 0:
                ansnegative = ansnegative | (1 << i)

        return -(ansnegative) if ansnegative != 0 else anspositive