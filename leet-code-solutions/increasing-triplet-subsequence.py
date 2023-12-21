class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1 = float('inf')
        m2 = float('inf')
        for num in nums:
            if num > m2:
                return True
            elif num <= m1:
                m1 = min(m1, num)
            elif num <= m2:
                m2 = min(m2, num)
        return False