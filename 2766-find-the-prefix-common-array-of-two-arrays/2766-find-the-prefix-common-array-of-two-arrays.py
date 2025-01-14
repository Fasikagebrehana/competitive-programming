class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        store = {}
        prefix = [0] * len(A)
        prefix[0] = 1 if A[0] == B[0] else 0

        store[A[0]] = 1
        if B[0] not in store:
            store[B[0]] = 1


        for i in range(1, len(A)):
            prefix[i] += prefix[i-1]
            if A[i] in store:
                prefix[i] += 1
            else:
                store[A[i]] = 1
            if B[i] in store:
                prefix[i] +=  1
            else:
                store[B[i]] = 1
        return prefix