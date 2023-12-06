class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        num1 = nums[0:n]
        num2 = nums[n:len(nums)]
        for i in range(n):
            ans.append(num1[i])
            ans.append(num2[i])
        return ans