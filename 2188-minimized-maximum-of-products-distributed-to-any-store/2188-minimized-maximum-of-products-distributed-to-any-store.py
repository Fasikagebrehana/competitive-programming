class Solution:
    def minimizedMaximum(self, n: int, nums: List[int]) -> int:
        def checker(middle):
            count = 0
            l = len(nums)
            for i in range(l):
                count += ceil(nums[i] / middle)
                if count > n:
                    return False
                
            return True

        answer = inf
        left, right = 1, max(nums) + 1
        while left <= right:
            middle = (left + right) // 2
            if checker(middle):
                answer = min(answer, middle)
                right = middle - 1
            else:
                left = middle + 1
        return answer