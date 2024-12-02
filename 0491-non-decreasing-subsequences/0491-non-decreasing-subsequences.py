class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer, arr = [], []
        n = len(nums)
        # visited = set()
        def backtrack(i):
            if i == n:
                # print(arr)
                if len(arr) > 1 and arr not in answer:
                    answer.append(arr.copy())
            #     print(answer)
                return
            if len(arr) >= 2 and arr not in answer:
                answer.append(arr.copy())
                
            
            for idx in range(i, len(nums)):
                if not arr or nums[idx] >= arr[-1]:
                    arr.append(nums[idx])
                    backtrack(idx+1)
                    arr.pop()
                        
                # else:
                #     arr.append(nums[idx])

                # if arr:
        backtrack(0)
        
        
        return answer