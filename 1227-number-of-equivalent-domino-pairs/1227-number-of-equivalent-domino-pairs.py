class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equivalent = 0
        n = len(dominoes)
        store = defaultdict(int)
        for i in range(n):
            a, b = dominoes[i]
            if (a,b) in store:
                store[(a,b)] += 1 
            elif (b, a) in store:
                store[(b, a)] += 1
            else:
                store[(a,b)] += 1

        for key, val in store.items():
            if val > 1:
                equivalent += (val* (val - 1)) // 2
        return equivalent
            