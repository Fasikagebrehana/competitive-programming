class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        dic = {}
        ans = 0
        for i in range(len(rolls)):
            if rolls[i] not in dic:
                dic[rolls[i]] = 1
            else:
                dic[rolls[i]] += 1
            
            if len(dic) == k:
                ans += 1
                dic.clear()
        return (ans + 1)
        