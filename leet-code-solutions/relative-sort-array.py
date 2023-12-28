class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    ans.append(arr1[j])
        res = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                res.append(arr1[i])
        res.sort()
        for i in range(len(res)):
            ans.append(res[i])
        return ans