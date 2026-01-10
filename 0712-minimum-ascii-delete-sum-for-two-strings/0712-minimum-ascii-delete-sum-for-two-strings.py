class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # print(ord('s'))
        # delete strings
        # we need to find the total summ of their ascii value of each array for the case if they can't  became equal it will return this
        store = {}

        s1Summ = [0] * len(s1)
        s2Summ = [0] * len(s2)
        
        summ = 0
        for i in range(len(s1)-1, -1, -1):
            summ += ord(s1[i])
            s1Summ[i] = summ

        summ = 0
        for j in range(len(s2) - 1, -1, -1):
            summ += ord(s2[j])
            s2Summ[j] = summ

        def dp(i, j):
            nonlocal summ
            if i >= len(s1) and j >= len(s2):
                return 0
            # one case is if s1 is finished and s2 isn't, which means we have to delete the rest of s2 and return our summ
            if i == len(s1):
                return s2Summ[j]
            if j == len(s2):
                return s1Summ[i]

            if (i,j) in store:
                return store[(i, j)]

            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            
            store[(i,j)] = min(ord(s1[i]) + dp(i+1, j), ord(s2[j]) + dp(i, j +1))
            return store[(i,j)]
        return dp(0, 0)
        # print(dp(0, 0))