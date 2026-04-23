class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        store = defaultdict(list)

        for i in range(len(nums)):
            store[nums[i]].append(i)
        
        for key, val in store.items():
            n = len(val)
            if n == 1:
                continue
            
            # we're doing substraction except self kind on the val list
            prefix = [0] * (n +1)
            for i in range(n):

                prefix[i+1] = prefix[i] + val[i]

            for i in range(n):
                index = val[i]
                # collect the sums of the differences which means (val[i]−val[0])+(val[i]−val[1])+...+(val[i]−val[i−1]) meaning val[i]⋅i−(val[0]+val[1]+...+val[i−1])

                leftside = (val[i] * i) - prefix[i]

                # for the rightsidekinda same but from right index
                rightside = (prefix[n] - prefix[i+1]) - (val[i] * (n-i-1))
                answer[index] = leftside + rightside
        return answer