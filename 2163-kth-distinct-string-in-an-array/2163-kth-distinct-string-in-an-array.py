class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        arr.sort(key=lambda x:counter[x])
        return arr[k-1] if counter[arr[k-1]] == 1 else ""