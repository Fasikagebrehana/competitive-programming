class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd = []
        maxx = 0
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxx = nums[i]
            prefixgcd.append(math.gcd(maxx, nums[i]))
        # print(prefixgcd)
        prefixgcd.sort()
        total = 0
        l, r = 0, len(prefixgcd) - 1
        while l < r:
            total += math.gcd(prefixgcd[l], prefixgcd[r])
            l += 1
            r -= 1
        return total