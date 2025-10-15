class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x+y=target
        # x=target-y
        answer = []
        store = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in store:
                answer.append(store[nums[i]])
                answer.append(i)
                
            store[target - nums[i]] = i
        
        return answer