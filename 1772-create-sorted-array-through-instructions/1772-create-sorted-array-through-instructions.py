class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = (10**9) + 7
        
        ans = 0
        arr = []
        for i in range(len(instructions)):
            to_right = len(arr) -  bisect_right(arr, instructions[i])
            to_left = bisect_left(arr, instructions[i])
            ans += min(to_left, to_right)

            arr.insert(bisect_left(arr, instructions[i]), instructions[i])
            

        return ans % mod