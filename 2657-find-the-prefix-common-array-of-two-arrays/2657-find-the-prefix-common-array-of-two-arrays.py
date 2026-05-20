class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = []
        b = []
        for i in range(len(A)):
            a.append((A[i], i))
            b.append((B[i], i))
        
        a.sort()
        b.sort()
        common = [0] * (len(a))
        for i in range(len(a)):
            common[max(a[i][1], b[i][1])] += 1
        # print(common)

        for i in range(1, len(a)):
            common[i] += common[i-1]
        return common