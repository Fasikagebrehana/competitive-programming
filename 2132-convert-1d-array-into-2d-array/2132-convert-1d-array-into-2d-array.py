class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []


        ans = []
        idx = 0
        j = 0
        for i in range(m):
            arr =[]
            while j < n and idx < len(original):
                arr.append(original[idx])
                
                idx += 1
                j += 1
            ans.append(arr.copy())
            j = 0
        return ans
            