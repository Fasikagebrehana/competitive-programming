class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [nums[0]]
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])

        # print(prefix)

        # print(suffix)
        
        for i in range(len(nums)-2, -1, -1):
            # print(i)
            suffix[i] = (suffix[i+1] * nums[i])

        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix[i+1])
            elif i == len(nums) - 1:
                answer.append(prefix[i-1])
            else:
                answer.append(prefix[i-1] * suffix[i+1])

        return answer