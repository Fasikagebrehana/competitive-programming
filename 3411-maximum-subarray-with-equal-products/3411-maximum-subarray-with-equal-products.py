class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_length = 0
        maxx = 0
        for i in range(len(nums)):
            prod = nums[i]
            gcd = nums[i]
            lcm = nums[i]
            for j in range(i+1, len(nums)):
                prod *=nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = math.lcm(lcm, nums[j])
                if prod == (gcd * lcm):
                    max_length = max(max_length, j-i + 1)
                    print(i, j)
        # print(max_length)
        return max_length