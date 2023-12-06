class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        n = len(nums)//3
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for num in dic:
            if dic[num] > n:
                ans.append(num)
        return ans