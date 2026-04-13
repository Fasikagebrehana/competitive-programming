class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = inf
        for i in range(len(nums)):
            if nums[i] == target:
                answer = min(answer, abs(i-start))
        
        return answer