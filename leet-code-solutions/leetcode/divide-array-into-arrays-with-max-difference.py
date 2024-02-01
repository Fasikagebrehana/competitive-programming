class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        print(nums)
        for i in range(0, len(nums), 3):
            ans.append(nums[i:i+3])
        for n1, n2, n3 in ans:
            if abs(n1 - n2) > k or abs(n2 - n3) > k or abs(n1 - n3) > k:
                return []
        return ans