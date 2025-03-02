class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)
        for id, val in nums1:
            store[id] += val

        for id, val in nums2:
            store[id] += val

        answer = []
        for key, val in store.items():
            answer.append([key, val])
        answer.sort()
        return answer