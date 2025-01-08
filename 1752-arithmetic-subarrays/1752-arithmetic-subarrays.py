class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            diff = None
            sorted_nums = sorted(nums[l[i]:r[i]+1])
            flag = True
            # print(sorted_nums)
            # print(l[i], r[i] + 1)
            for j in range(len(sorted_nums) - 1):
                if diff is None:
                    diff = sorted_nums[j+1] - sorted_nums[j]
                else:
                    if diff != sorted_nums[j+1] - sorted_nums[j]:
                        answer.append(False)
                        flag = False
                        break
            if flag:
                answer.append(True)
        
        return answer