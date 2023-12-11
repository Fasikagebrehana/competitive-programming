class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        n = len(arr)
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic:
            if dic[key] > n//4:
                return key
        return 0