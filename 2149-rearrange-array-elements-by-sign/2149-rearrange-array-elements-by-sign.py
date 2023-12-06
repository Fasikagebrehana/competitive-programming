class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [x for x in nums if x > 0]
        negative = [y for y in nums if y < 0]
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
        