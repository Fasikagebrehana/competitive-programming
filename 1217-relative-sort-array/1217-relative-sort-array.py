class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for i in range(len(arr2)):
            for j in range(counter[arr2[i]]):
                ans.append(arr2[i])
        extra = []
        for num in arr1:
            if num not in arr2:
                extra.append(num)
        extra.sort()
        ans.extend(extra)
        return ans