class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)

        nums = set(nums)
        answer = []
        if len(nums) == length:
            return []
        for i in range(1,length+1):
            # print(i)
            if i not in nums:
                answer.append(i)
        return answer