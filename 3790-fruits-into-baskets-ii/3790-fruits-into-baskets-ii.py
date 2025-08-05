class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        taken = [False] * len(fruits)

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i] and taken[j] != True:
                    taken[j] = True
                    break
        return taken.count(False)