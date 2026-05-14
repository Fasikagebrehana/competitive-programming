class Solution:
    def isGood(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        n = max(nums)
        for num in range(1, n+1):
            if num == n:
                if counter[num] != 2:
                    return False
            else:
                if counter[num] > 1 or counter[num] < 1:
                    return False
        return True