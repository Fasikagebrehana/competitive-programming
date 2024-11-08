class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        anded = 1
        arr = []
        for i in range(len(nums)):
            temp = format(nums[i], '024b')
            arr.append(temp)
        # print(arr)
        ans = 0
        for i in range(24):
            count = 0
            for j in range(len(nums)):
                if arr[j][i] == '1':
                    count += 1
            ans = max(ans, count)
            # print(count)
        return ans