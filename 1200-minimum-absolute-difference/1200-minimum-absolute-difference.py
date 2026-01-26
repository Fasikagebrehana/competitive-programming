class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # finding the min difference
        # key: val
        store = defaultdict(list)
        arr.sort()
        minDiff = inf
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] <= minDiff:
                store[arr[i+1] - arr[i]].append((arr[i],arr[i+1] ))
                minDiff = arr[i+1] - arr[i]

        store = dict(sorted(store.items()))
        # print(store)
        for key, val in store.items():
            return val