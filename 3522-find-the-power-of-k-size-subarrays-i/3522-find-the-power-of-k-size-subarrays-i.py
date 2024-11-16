class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(0, k-1):
            if nums[i+1] != nums[i] + 1 or nums[i] >= nums[i+1]:
                answer.append(-1)
                break
        else:
            answer.append(nums[k-1])
        left = 1
        for i in range(k, len(nums)):
            for j in range(left, i):
                if nums[j] + 1 != nums[j+1]:
                    answer.append(-1)
                    break
            else:
                answer.append(nums[i])
            left += 1
        return answer