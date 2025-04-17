class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        answer = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j) % k ==0:
                    answer += 1
        return answer