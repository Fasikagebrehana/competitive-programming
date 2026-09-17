class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # answers = []
        # arr.sort()
        l, r = 0, 0
        curr_sum = 0
        prefix = [inf] *len(arr)
        suffix = [inf] *len(arr)

        while r < len(arr):
            curr_sum += arr[r]

            while curr_sum > target and l <= r:
                curr_sum -= arr[l]
                l += 1
            if curr_sum == target:
                prefix[r] = (r-l+1)


            if r > 0:
                prefix[r] = min(prefix[r], prefix[r-1])
            r += 1

        # print(prefix)
       
        l= r= (len(arr) - 1)
        curr_sum = 0
        while r >= 0:
            curr_sum += arr[r]

            while curr_sum > target and l >= r:
                curr_sum -= arr[l]
                l -= 1
            if curr_sum == target:
                suffix[r] = (l-r+1)



            if r < (len(arr) - 1):
                suffix[r]= min(suffix[r], suffix[r + 1])

            r -= 1
        
        # print(suffix)
        # the idea is to find the minimum sum from the prefix up to index and suffix of the next index
        answer = inf
        for i in range(len(arr) - 1):
            if prefix[i] != inf and suffix[i + 1] != inf:
                answer = min(answer, prefix[i]+ suffix[i+1])
        return answer if answer!= inf else -1